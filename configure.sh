#install guidelines followed from http://www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/

#Run the following separately
# virtualenv and virtualenvwrapper
#rm -rf ~/.virtualenvs
#export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
#export WORKON_HOME=$HOME/.virtualenvs
#source /usr/local/bin/virtualenvwrapper.sh
#mkvirtualenv --python=/usr/bin/python3 cv

pip3 install -r requirements.txt
cd external/opencv && git checkout 3.1.0 && cd -
cd external/opencv_contrib && git checkout 3.1.0 && cd -
rm -rf external/opencv/build
mkdir -p external/opencv/build/install
cd external/opencv/build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local\
	-D INSTALL_C_EXAMPLES=OFF \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
	-D BUILD_EXAMPLES=ON \
	-D PYTHON_EXECUTABLE=/home/shobhit/.virtualenvs/cv/bin/python ..
make -j4
sudo make install
sudo ldconfig

cd ~/.virtualenvs/cv/lib/python3.4/site-packages/
ln -s /usr/local/lib/python3.4/site-packages/cv2.cpython-34m.so cv2.so
workon cv
