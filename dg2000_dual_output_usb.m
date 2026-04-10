%% DG2000 USB 双通道输出示例
% 功能：
% 1) CH1 输出可调正弦波
% 2) CH2 同时输出 0~5V 方波脉冲（用于与采集器通信）
%
% 使用前准备：
% - MATLAB 安装 Instrument Control Toolbox
% - 通过 USB 连接波形发生器
% - 建议先在设备面板确认通道与负载设置

clear; clc;

%% ====== 参数区（按需修改）======
cfg = struct();

% 连接参数
cfg.resourceName = "";   % 留空则自动选择第一个 USB 设备；也可手填如 "USB0::0x1AB1::0x0641::DG2E123456789::INSTR"
cfg.doReset = false;      % true: 连接后执行 *RST（会重置仪器状态）

% CH1：正弦波参数
cfg.ch1FreqHz = 1000;     % 频率 (Hz)
cfg.ch1Vpp = 2.0;         % 幅值 (Vpp)
cfg.ch1OffsetV = 0.0;     % 偏置 (V)
cfg.ch1PhaseDeg = 0;      % 相位 (deg)

% CH2：方波脉冲参数（0~5V）
cfg.ch2PulseFreqHz = 1000;    % 脉冲重复频率 (Hz)
cfg.ch2PulseWidthS = 100e-6;  % 脉宽 (s)
cfg.ch2LowV = 0.0;            % 低电平 (V)
cfg.ch2HighV = 5.0;           % 高电平 (V)

% 输出负载设置：
% "INF" 表示高阻负载模式，常用于接采集器高阻输入，电压更接近设定值
% "50"  表示 50 欧负载模式
cfg.outputLoad = "INF";

%% ====== 主流程 ======
try
    dev = connectAwg(cfg.resourceName);
    cleanupObj = onCleanup(@() safeDisconnect(dev)); %#ok<NASGU>

    idn = strtrim(writeread(dev, "*IDN?"));
    fprintf("已连接设备: %s\n", idn);

    writeline(dev, "*CLS");
    if cfg.doReset
        writeline(dev, "*RST");
        pause(0.5);
    end

    % 先关输出，避免参数切换时误触发
    writeline(dev, ":OUTP1 OFF");
    writeline(dev, ":OUTP2 OFF");

    % 通道负载模式
    writeline(dev, sprintf(":OUTP1:LOAD %s", cfg.outputLoad));
    writeline(dev, sprintf(":OUTP2:LOAD %s", cfg.outputLoad));

    % CH1: 正弦波
    writeline(dev, sprintf(":SOUR1:APPL:SIN %.12g,%.12g,%.12g", ...
        cfg.ch1FreqHz, cfg.ch1Vpp, cfg.ch1OffsetV));
    writeline(dev, sprintf(":SOUR1:PHAS %.12g", cfg.ch1PhaseDeg));

    % CH2: 脉冲波（0~5V）
    % 使用 PULSE 模式可以直接设高低电平和脉宽，便于和采集器通信
    writeline(dev, ":SOUR2:FUNC PULS");
    writeline(dev, sprintf(":SOUR2:FREQ %.12g", cfg.ch2PulseFreqHz));
    writeline(dev, sprintf(":SOUR2:PULS:WIDT %.12g", cfg.ch2PulseWidthS));
    writeline(dev, sprintf(":SOUR2:VOLT:LOW %.12g", cfg.ch2LowV));
    writeline(dev, sprintf(":SOUR2:VOLT:HIGH %.12g", cfg.ch2HighV));

    % 连续输出模式
    writeline(dev, ":SOUR1:BURS:STAT OFF");
    writeline(dev, ":SOUR2:BURS:STAT OFF");

    % 尽量同时开启两个通道
    writeline(dev, ":OUTP1 ON");
    writeline(dev, ":OUTP2 ON");

    fprintf("CH1 正弦波已开启: f=%.3f Hz, Vpp=%.3f V, Offset=%.3f V\n", ...
        cfg.ch1FreqHz, cfg.ch1Vpp, cfg.ch1OffsetV);
    fprintf("CH2 脉冲已开启: f=%.3f Hz, Width=%.6g s, Low=%.3f V, High=%.3f V\n", ...
        cfg.ch2PulseFreqHz, cfg.ch2PulseWidthS, cfg.ch2LowV, cfg.ch2HighV);

    % 读取并打印一条系统错误信息（0 表示无错误）
    err = strtrim(writeread(dev, ":SYST:ERR?"));
    fprintf("设备状态: %s\n", err);

catch ME
    fprintf(2, "执行失败: %s\n", ME.message);
    fprintf(2, "建议检查: USB 连接、resourceName、仪器是否支持这些 SCPI 命令。\n");
end

%% ====== 本文件内的本地函数 ======
function dev = connectAwg(resourceName)
    if strlength(resourceName) == 0
        devs = visadevlist;
        if isempty(devs)
            error("未发现 VISA 设备。请确认已安装驱动并连接仪器。");
        end

        % 优先选择 USB 设备
        idx = find(contains(string(devs.ResourceName), "USB", "IgnoreCase", true), 1, "first");
        if isempty(idx)
            idx = 1;
        end
        resourceName = string(devs.ResourceName(idx));
        fprintf("自动选择资源: %s\n", resourceName);
    end

    dev = visadev(resourceName);
    configureTerminator(dev, "LF");
    dev.Timeout = 8;
end

function safeDisconnect(dev)
    if ~isempty(dev)
        try
            clear dev;
        catch
            % 忽略清理阶段异常
        end
    end
end
