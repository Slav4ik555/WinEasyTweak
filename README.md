# WinEasyTweak

![Python](https://img.shields.io/badge/Python-3.7%2B-blue) ![CustomTkinter](https://img.shields.io/badge/CustomTkinter-UI-yellowgreen)

![Screenshot](https://github.com/Slav4ik555/WinEasyTweak/blob/master/assets/img/screenshot.png)

## ✨Features

- **Windows Debloating**: Remove pre-installed Windows bloatware and enhance privacy by disabling telemetry.
- **Windows/Office Activation**: Activate Microsoft products.
- **Runtime Libraries**: Install all required Microsoft Visual C++ redistributables.
- **Lightweight Interface**: Simple and intuitive GUI.

## ⚙️Requirements

- Windows 10/11
- Internet connection

## 🚀Usage

1. Download the latest executable from [Releases](https://github.com/yourusername/WinEasyTweak/releases).
2. Run `WinEasyTweak.exe` (Administrator rights required).

**The interface provides three main functions:**

1. **Debloat Windows**:
  
  - Runs Raphire's Win11Debloat script.
  - Uses [default settings](https://github.com/Raphire/Win11Debloat?tab=readme-ov-file#changes-included-in-the-default-mode) with silent mode.
2. **Activate Windows/Office**:
  
  - Uses MAS (Microsoft Activation Scripts) from [massgravel/MAS](https://github.com/massgravel/Microsoft-Activation-Scripts).
  - Supports both Windows and Office activation.
3. **Install Redistributables**:
  
  - Downloads and installs latest version of Microsoft Visual C++ redistributables.

## ⚠️Important Notes

- Run as Administrator.
- Internet connection is required for all operations.
- Antivirus may flag activation scripts (false positive).
- Create a system restore point before debloating.

## 🔌Used Components

| Function | Source | License |
| --- | --- | --- |
| Debloating | [Raphire/Win11Debloat](https://github.com/Raphire/Win11Debloat) | MIT |
| Activation | [massgravel/MAS](https://github.com/massgravel/Microsoft-Activation-Scripts) | GPL-3.0 license |
| VC++ Runtimes | [abbodi1406/vcredist](https://github.com/abbodi1406/vcredist) | Unlicense license |

## ⚠️Disclaimer

**❗Use at your own risk!❗**

- This tool executes third-party scripts.
- Debloating may remove Store apps you actually use (can be reinstalled via Microsoft Store).
- Activation methods may violate Microsoft's terms.
- Developer is not responsible for any system instability or legal issues.

## 📜License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
