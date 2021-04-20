
# Example with CPUs=2, GPUs=0, HORIZON=10000, ROLLOUT=1, EXP_NAME="test_1", RENDER=true, SIM_STEP=0.01, TRAINING_ITERATION=100, 
# COLS=1, ROWS=1, LANES=1, BASELINE=true, TL_TYPE="controlled", WAYS={"top":0, "bot":5, "left":5, "right":0}, PROB=0.0, MAX_GAP=default,
# DETECTOR_GAP=default

echo "Generating test_1 configuration..."
python config_generator.py -o ./ -cpus 2 -gpus 0 -hor 10000 -rol 1 -n test_1 -r -s 0.01 -i 100 -net [1,1] -l 1 -b -tl controlled -f [0,5,5,0] -p 0.0

# Example with CPUs=2, GPUs=0, HORIZON=10000, ROLLOUT=1, EXP_NAME="test_2", RENDER=false, SIM_STEP=0.01, TRAINING_ITERATION=100, 
# COLS=2, ROWS=2, LANES=1, BASELINE=true, TL_TYPE="controlled", WAYS={"top":5, "bot":5, "left":5, "right":5}, PROB=0.0, MAX_GAP=default,
# DETECTOR_GAP=default

echo "Generating test_2 configuration..."
python config_generator.py -o ./ -cpus 2 -gpus 0 -hor 10000 -rol 1 -n test_2 -s 0.01 -i 100 -net [2,2] -l 1 -b -tl controlled -f [5,5,5,5] -p 0.0

# Example with CPUs=2, GPUs=0, HORIZON=10000, ROLLOUT=1, EXP_NAME="test_3", RENDER=false, SIM_STEP=0.01, TRAINING_ITERATION=100, 
# COLS=1, ROWS=1, LANES=1, BASELINE=false, TL_TYPE="static", WAYS={"top":0, "bot":1, "left":0, "right":0}, PROB=0.75, MAX_GAP=default,
# DETECTOR_GAP=default

echo "Generating test_3 configuration..."
python config_generator.py -o ./ -cpus 2 -gpus 0 -hor 10000 -rol 1 -n test_3 -s 0.01 -i 100 -net [1,1] -l 1 -tl static -f [0,1,0,0] -p 0.75

# Example with CPUs=2, GPUs=0, HORIZON=10000, ROLLOUT=1, EXP_NAME="test_3", RENDER=false, SIM_STEP=0.01, TRAINING_ITERATION=100, 
# COLS=1, ROWS=1, LANES=1, BASELINE=true, TL_TYPE="static", WAYS={"top":0, "bot":1, "left":0, "right":0}, PROB=0.75, MAX_GAP=4.0,
# DETECTOR_GAP=1.2

echo "Generating test_4 configuration..."
python config_generator.py -o ./ -cpus 2 -gpus 0 -hor 10000 -rol 1 -n test_4 -s 0.01 -i 100 -net [1,1] -l 1 -b -tl actuated -mg 4.0 -dg 1.2 -f [0,1,0,0] -p 0.75

# Example with CPUs=default, GPUs=default, HORIZON=default, ROLLOUT=default, EXP_NAME="test_5", RENDER=default, SIM_STEP=default, TRAINING_ITERATION=default, 
# COLS=default, ROWS=default, LANES=default, BASELINE=default, TL_TYPE=default, WAYS={"top":default, "bot":default, "left":default, "right":default}, 
# PROB=default, MAX_GAP=default, DETECTOR_GAP=default

echo "Generating test_5 configuration..."
python config_generator.py -o ./ -n test_5
