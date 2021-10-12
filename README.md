# ZJU_PunchClock

* [ZJU_PunchClock](#zju_punchclock)
   * [If you want to start using released APP](#if-you-want-to-start-using-released-app)
      * [Download the right version of this software](#download-the-right-version-of-this-software)
      * [Install the chromedriver](#install-the-chromedriver)
      * [Run the program](#run-the-program)
   * [If you want to start from Scratch](#if-you-want-to-start-from-scratch)
      * [Clone the repository](#clone-the-repository)
      * [Install the dependencies on your python](#install-the-dependencies-on-your-python)
      * [Install the chromedriver](#install-the-chromedriver-1)
      * [Run the program](#run-the-program-1)

Before you started, you need to guarantee that you’ve already installed `python3` and `pip3`.

## If you want to start using released APP

### Download the right version of this software

Please go to the [GitHub Release Website](https://github.com/BiEchi/ZJU_PunchClock/releases/tag/v1.0) to download the right version of your app.

### Install the `chromedriver`

We assume that you’ve already installed `Chrome` on your computer. If you haven’t, go to the [Official Web](https://www.google.cn/intl/zh-CN/chrome/) to download it.

**Install the Chrome driver**

You also need to install `chromedriver` into your system `PATH`.

**Before started**

Before you install the chromedriver, you should have:

![before started](./images/readme_about/before_started.png)

Then you need to install the `chromedriver`. 

**Check for the right version of Chrome**

Please open the current Chrome (if you have) and check which version you're in. For example, mine is 94.0.4606.

![check for right version](./images/readme_about/check_for_right_version.png)

 **Download the correct version of chromedriver**

Go to [the download website](https://chromedriver.chromium.org/) to download the correct version of ChromeDriver. If you're using Windows, make sure you download the Windows version. I'm using Mac, so I'll download the Mac version.

![correct version](./images/readme_about/correct_version.png)After downloading, please unzip the file and move it to your system PATH.

![move into PATH](./images/readme_about/move_into_path.png)

Then please check whether you've successfully installed your chromedriver. If you see the feedback below, you're all set.

![examine](./images/readme_about/examine.png)

Notes:

\-   You must download exactly the same version of `chromedriver` as your chrome browser if you want to use the `chromedriver` as your selenium driver. The chrome browser on your machine is likely to be updated automatically when a new version is released. In this case, please update to the newest version of `chromedriver` too.

\-   I strongly recommend you to install the `chromedriver` into the system software directory immediately, i.e. it should appear in `/usr/local/bin/chromedriver`.

### Run the program

Just double-click on the program and it will automatically ask you to enter your account and password for logging in.

---



## If you want to start from Scratch

### Clone the repository

```shell
git clone https://github.com/BiEchi/ZJU_PunchClock
```

### Install the dependencies on your python

```shell
pip3 install selenium
pip3 install time
pip3 install configparser
```

### Install the `chromedriver`

We assume that you’ve already installed `Chrome` on your computer. If you haven’t, go to the [Official Web](https://www.google.cn/intl/zh-CN/chrome/) to download it.

**Install the Chrome driver**

You also need to install `chromedriver` into your system `PATH`.

**Before started**

Before you install the chromedriver, you should have:

![before started](./images/readme_about/before_started.png)

Then you need to install the `chromedriver`. 

**Check for the right version of Chrome**

Please open the current Chrome (if you have) and check which version you're in. For example, mine is 94.0.4606.

![check for right version](./images/readme_about/check_for_right_version.png)

 **Download the correct version of chromedriver**

Go to [the download website](https://chromedriver.chromium.org/) to download the correct version of ChromeDriver. If you're using Windows, make sure you download the Windows version. I'm using Mac, so I'll download the Mac version.

![correct version](./images/readme_about/correct_version.png)After downloading, please unzip the file and move it to your system PATH.

![move into PATH](./images/readme_about/move_into_path.png)

Then please check whether you've successfully installed your chromedriver. If you see the feedback below, you're all set.

![examine](./images/readme_about/examine.png)

Notes:

\-   You must download exactly the same version of `chromedriver` as your chrome browser if you want to use the `chromedriver` as your selenium driver. The chrome browser on your machine is likely to be updated automatically when a new version is released. In this case, please update to the newest version of `chromedriver` too.

\-   I strongly recommend you to install the `chromedriver` into the system software directory immediately, i.e. it should appear in `/usr/local/bin/chromedriver`.

### Run the program

At last, just run the `main.py` program.

```shell
python3 main.py
```

