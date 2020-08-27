### macOS

Crash logs are in `~/Library/Logs/DiagnosticReports`. The following command will list the crash reports for a SuperCollider program with the most recent first:

    ls -lt ~/Library/Logs/DiagnosticReports | grep -E 'SuperCollider|sclang|scsynth|supernova'

If the app is hanging, and you think you know which one it is, you can force it to crash and produce a log by sending it a segfault signal:

    pkill -SIGSEGV <sc-executable> # may need to execute twice to force a crash

The crash log will be placed in `~/Library/Logs/DiagnosticReports` with the others.

### Linux

A core dump file is generated when an application crashes. See [this helpful article](https://linux-audit.com/understand-and-configure-core-dumps-work-on-linux/) for information on core dumps and how to enable them on your machine. You don't need to send us the full core dump (it will probably be quite large), but you can generate a helpful backgrace with gdb:

    gdb <sc-executable> <core-file> -ex where -ex quit

See `man gdb` for more information on using core files.

For a hanging process, you can use the command `pkill -SIGSEGV <sc-executable>` to force a crash, which will then produce a core dump.

### Windows

We don't currently have an easy way to get good crash log information on Windows. You can view logs in Event Viewer, but there's not enough information there that would be helpful for us. If you know of an easy way to get a high-quality crash report on Windows, let us know!

If you have a reproducible crash, you can attach to the crashing process using Visual Studio or one of the [Windows debuggers](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/).

For example, to use CDB.exe to debug a crash in sclang.exe, first attach to sclang.exe using:

    "C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\cdb.exe" -pn sclang.exe

Then type `g<enter>` to continue running until you hit the crash. Once the crash is hit, type `k<enter>` to generate a backtrace at the crash site.



