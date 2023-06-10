from checkout import checkout


path_dir = "/home/marina/tst"
path_arx = "/home/marina/arx2.7z"
path_to_dir = "/home/user/out"


def test_step1():
    assert checkout("cd {}; 7z a {}".format(path_dir, path_arx), "Everything is Ok"), "Test1 Fail"

def test_step2():
    assert checkout("cd {}; 7z u {}".format(path_dir, path_arx), "Everything is Ok"), "Test1 Fail"

def test_step3():
    assert checkout("cd {}; 7z d {}".format(path_dir, path_arx), "Everything is Ok"), "Test1 Fail"

def test_step4():
    assert checkout("cd {}; 7z e {} -o{}".format(path_dir, path_arx, path_to_dir), "ERRORS:"), "Test1 Fail"

def test_step5():
    assert checkout("cd {}; 7z t {}".format(path_dir, path_arx), "Everything is Ok"), "Test1 Fail"

def test_step6():
    assert checkout("cd {}; 7z l{}".format(path_dir, path_arx), "test1.sh"), "Test6 Fail"

def test_step7():
    assert checkout("cd {}; 7z x{}".format(path_dir, path_arx, path_dir), "Extracting"), "Test7 Fail"