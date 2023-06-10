import subprocess

if __name__ == '__main__':
    result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    out = result.stdout
    out_array = out.split('\n')

    if result.returncode == 0:
        if 'VERSION="20.04.1 LTS (Focal Fossa)"' in out_array and 'VERSION_CODENAME=focal' in out_array:
            print(out)
        else:
            print("FAIL")
    else:
        print("FAIL")


