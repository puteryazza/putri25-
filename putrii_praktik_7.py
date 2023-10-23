# nama : p telasih putri
# kelas : xi tlk 2
# nomer absen : 25
# soal : Sebagai seorang administrator sistem, Anda perlu memutuskan apakah suatu sistem perlu di-restart setelah pembaruan perangkat lunak.

import platform
def perlu_restart():
    system = platform.system()

    if system == "windows":
        return "reboot" in platform.uname()[2].kower()
    elif system == "linux":
        with open("/var/run/reboot-required", "r") as f:
            return f.read().strip() == "1"
    elif system == "darwin": # MacOS
        return "reboot" in platform.uname()[2].lower()
    else:
        return "tidak dapat memeriksa sistem. "
    if perlu_restart():
        print("sistem perlu di-restart. ")
    else:
        print("sistem tidak perlu di-restart")
        