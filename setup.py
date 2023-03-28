from setuptools import setup
# from setuptools import find_packages
setup(
    name="MSIcal",
    version="2023.03",
    author="dming",
    author_email="dongliulou@126.com",  # 作者邮箱
    url='',  # github或者自己的网站地址
    description="calculate MSI status based on mutations",
    long_description=open('README.txt').read(),  #读取文件中介绍包的详细内容
    long_description_content_type="text/markdown",  # 指定详细描述的文本格式
    python_requires=">=3.6.0",  # python依赖版本
    license="MIT Licence",  # 指定许可证
    install_requires=[""],  # 需要安装的依赖,如["matplotlib", "talib", "pylab", "numpy", "pandas", "baostock"]
    package_dir={"": "src"},
    package_data={
        "MSIcal": ["*.yaml"],
    },
    packages=[
        "MSIcal",
    ],  # 打包目录下的指定模块
    # packages=find_packages(),  # 打包目录下的全部模块
    # packages=find_packages(exclude=["test", "test.*"])			# 打包除了指定模块的全部模块
    include_package_data = True,									# 打包路径下的其他文件
    platforms="any",  # 程序适用的软件平台列表
)