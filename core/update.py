import subprocess


def update():
    git = subprocess.Popen(['git', 'pull'])
    git.wait()

if __name__ == '__main__':
    update()
    update_sub()
