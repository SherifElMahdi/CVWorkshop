RUN /root/anaconda3/envs/cntk-py35/bin/conda install -y -n cntk-py35 cython boost opencv cmake
RUN bash -c 'source /cntk/activate-cntk && pip install easydict pyyaml dlib'
RUN bash -c 'source /cntk/activate-cntk && cd /cntk/Examples/Image/Detection/utils && git clone https://github.com/CatalystCode/py-faster-rcnn.git && cd py-faster-rcnn/lib && python setup.py build_ext --inplace'
RUN cp /cntk/Examples/Image/Detection/utils/py-faster-rcnn/lib/pycocotools/_mask.cpython-35m-x86_64-linux-gnu.so /cntk/Examples/Image/Detection/utils/cython_modules/ 
RUN cp /cntk/Examples/Image/Detection/utils/py-faster-rcnn/lib/utils/cython_bbox.cpython-35m-x86_64-linux-gnu.so /cntk/Examples/Image/Detection/utils/cython_modules/ 
RUN cp /cntk/Examples/Image/Detection/utils/py-faster-rcnn/lib/nms/gpu_nms.cpython-35m-x86_64-linux-gnu.so /cntk/Examples/Image/Detection/utils/cython_modules/ 
RUN cp /cntk/Examples/Image/Detection/utils/py-faster-rcnn/lib/nms/cpu_nms.cpython-35m-x86_64-linux-gnu.so /cntk/Examples/Image/Detection/utils/cython_modules/ 