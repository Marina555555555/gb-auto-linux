import subprocess

if __name__ == '__main__':

    def func(com: str, text: str):
        result = subprocess.run(com, shell=True,
                                stdout=subprocess.PIPE, encoding='utf 8')
        out = result.stdout
        # print(out)
        if result.returncode == 0:
            if text in out:
                print(True)
            else:
                print(False)
        else:
            print(False)


    func('cat /etc/os-release', 'focal')