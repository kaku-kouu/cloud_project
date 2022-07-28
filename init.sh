cd plane_source
git clone https://github.com/STORM-IRIT/Plane-Detection-Point-Cloud.git
cd Plane-Detection-Point-Cloud

sudo apt-get install libcgal-dev

set -ex

# CGAL is the only required dependency
sudo apt-get install libcgal-dev

# compile the code
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j
cd ..
cd ..