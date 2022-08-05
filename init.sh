
# sudo apt-get update
# sudo apt-get install build-essential cmake  lzip
# sudo apt-get install m4 m4-doc
# sudo apt-get install libgmpxx4ldbl 

# wget https://gmplib.org/download/gmp/gmp-6.2.1.tar.lz
# tar --lzip -xvf gmp-6.2.1.tar.lz 
# cd gmp-6.2.1/
# ./configure --enable-cxx
# make 
# sudo make install

# conda init
# source ~/.bashrc
# conda deactivate

# mkdir plane_source2
# cd plane_source2

# wget https://github.com/CGAL/cgal/archive/refs/tags/v5.1.5.zip
# unzip v5.1.5.zip
# cd cgal-5.1.5/
# mkdir build
# cd build
# cmake -DCGAL_HEADER_ONLY=OFF -DCMAKE_BUILD_TYPE=Release ..                        # 
# make                                                                              #
# make install  
# cd ..
# cd ..



git clone https://github.com/STORM-IRIT/Plane-Detection-Point-Cloud.git
cd Plane-Detection-Point-Cloud


set -ex
# CGAL is the only required dependency
#sudo apt-get install libcgal-dev

# compile the code
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j
cp pdpc* ../../../executable2/
cd ..
cd ..
#cd figures
#./generate.sh

conda activate azureml_py38

