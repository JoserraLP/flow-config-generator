# flow-config-generator
Generator script of the configuration files needed to run a simulation on Eclipse Sumo's Flow Framework.

The generated file will be located at the route indicated on the first param and will contain the following schema:

{     
&nbsp;&nbsp; "GLOBAL" : {     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "CPUS": val,     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "GPUS": val,    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "HORIZON": val,     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "ROLLOUTS": val,     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "EXP_NAME": "experiment_name"    
&nbsp;&nbsp; },      
&nbsp;&nbsp; "SIM": {      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "SIM_STEP": val,     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "RENDER": true/false      
&nbsp;&nbsp; },     
&nbsp;&nbsp; "EXPERIMENT": {     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "TRAINING_ITERATION": val      
&nbsp;&nbsp; },     
&nbsp;&nbsp; "NETWORK": {      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "COLS": val,      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "ROWS": val,      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "LANES": val      
&nbsp;&nbsp; },      
&nbsp;&nbsp; "TL": {      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "BASELINE": true/false,     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "TL_TYPE": "val",      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "MAX_GAP": val,    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "DETECTOR_GAP": val    
&nbsp;&nbsp; },   
&nbsp;&nbsp; "FLOW": {    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "WAYS": {    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "top": val,    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "bot": val,    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "left": val,    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "right": val    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; },    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "PROB": val   
&nbsp;&nbsp; }   
}    

Note: both MAX_GAP and DETECTOR_GAP are optional depending on the value of TL_TYPE.

## Installation

## Usage
