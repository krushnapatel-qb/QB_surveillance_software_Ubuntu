#define MyAppName "Quantumbot"
#define MyAppVersion "0.1"
#define MyAppPublisher "Quantumbot"
#define MyAppURL "https://quantumbot.in/"
#define MyAppExeName "Quantumbot.exe"
#define MyAppAssocName MyAppName + " File"
#define MyAppAssocExt ".myp"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt

[Setup]
AppId={{7F670680-802D-4AE5-B642-22BA5D7347DC}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName=C:\{#MyAppName}
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
ChangesAssociations=yes
DisableProgramGroupPage=yes
OutputBaseFilename=qb
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; 

[Files]
Source: "D:\surveillance_software\dist\Quantumbot.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\surveillance_software\media\logo\qb-light.png"; DestDir: "{app}\media"; Flags: ignoreversion recursesubdirs createallsubdirs

[Registry]
; Add the application to startup automatically after installation
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "{#MyAppName}"; ValueData: """{app}\{#MyAppExeName}"""; Flags: uninsdeletevalue

[Icons]
; Create a desktop icon for the application
Name: "{autodesktop}\QuantumBot"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "D:\surveillance_software\media\icon\icon.ico";

[Run]
; Run the application after installation
Filename: "{app}\{#MyAppExeName}"; Description: "Launch My Application"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: files; Name: "{userappdata}\My Application\*"

[Code]
var
  PasswordPage: TInputQueryWizardPage;
  UserPassword: String;
  CustomPassword: String;

procedure InitializeWizard;
begin
  // Define your custom password here
  CustomPassword := 'tipl#789'; // Set your custom password

  // Create a password input page
  PasswordPage := CreateInputQueryPage(wpWelcome,
    'Password Required', 'Please enter the installation password',
    'You must enter the correct password to continue with the installation.');
  PasswordPage.Add('Password:', True); // True indicates a masked (password) input box
end;

function NextButtonClick(CurPageID: Integer): Boolean;
begin
  if CurPageID = PasswordPage.ID then
  begin
    UserPassword := PasswordPage.Values[0];
    if UserPassword <> CustomPassword then
    begin
      MsgBox('The password you entered is incorrect. Please try again.', mbError, MB_OK);
      Result := False;
    end else
    begin
      Result := True;
    end;
  end else
    Result := True;
end;

function AskPassword(): Boolean;
var
  Form: TSetupForm;
  OKButton, CancelButton: TButton;
  PwdEdit: TPasswordEdit;
begin
  Result := false;
  Form := CreateCustomForm();
  try
    Form.ClientWidth := ScaleX(256);
    Form.ClientHeight := ScaleY(100);
    Form.Caption := 'Uninstall Password';
    Form.BorderIcons := [biSystemMenu];
    Form.BorderStyle := bsDialog;

    OKButton := TButton.Create(Form);
    OKButton.Parent := Form;
    OKButton.Width := ScaleX(75);
    OKButton.Height := ScaleY(23);
    OKButton.Left := Form.ClientWidth - ScaleX(75 + 6 + 75 + 50);
    OKButton.Top := Form.ClientHeight - ScaleY(23 + 10);
    OKButton.Caption := 'OK';
    OKButton.ModalResult := mrOk;
    OKButton.Default := true;

    CancelButton := TButton.Create(Form);
    CancelButton.Parent := Form;
    CancelButton.Width := ScaleX(75);
    CancelButton.Height := ScaleY(23);
    CancelButton.Left := Form.ClientWidth - ScaleX(75 + 50);
    CancelButton.Top := Form.ClientHeight - ScaleY(23 + 10);
    CancelButton.Caption := 'Cancel';
    CancelButton.ModalResult := mrCancel;
    CancelButton.Cancel := True;

    PwdEdit := TPasswordEdit.Create(Form);
    PwdEdit.Parent := Form;
    PwdEdit.Width := ScaleX(210);
    PwdEdit.Height := ScaleY(23);
    PwdEdit.Left := ScaleX(23);
    PwdEdit.Top := ScaleY(23);

    Form.ActiveControl := PwdEdit;

    if Form.ShowModal() = mrOk then
    begin
      Result := PwdEdit.Text = 'tipl#789';
      if not Result then
            MsgBox('Password incorrect: Uninstallation prohibited.', mbInformation, MB_OK);
    end;
  finally
    Form.Free();
  end;
end;


function InitializeUninstall(): Boolean;
begin
  Result := AskPassword();
end;  