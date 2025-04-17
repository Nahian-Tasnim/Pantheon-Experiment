# Pantheon Congestion Control Evaluation
This repository contains an experimental result analysis using the StanfordSNR Pantheon framework to evaluate congestion control algorithms (Cubic, BBR, and Vegas) under different network conditions using Mahimahi. 

## Modifications:
Some modification was made in the existing Pantheon framework.
1. Minor modification to handle the errors raised during the experiment.
2. Modification was done in the test.py to produce text log files containing throughput, rtt and loss for each scheme in desired format.
3. Changed the whole analyze.py to produce the desired graphs.

## Project Structure:
Pantheon-Experiment:
1. graphs                   # Generated graphs for each scenario
2. results
   => high_latency          # Results of 1 Mbps, 200 ms RTT condition
   => low_latency           # Results of 50 Mbps, 10 ms RTT condition
3. analyze.py               # Modified analysis script for generating graphs
4. command_log.pdf          # Linux terminal command log for replication
5. report.pdf               # Detailed experimental report

## Replication Instructions:
1. Install required dependencies.
2. Clone pantheon.
3. Install Python 2.7.18
4. Install pip for Python 2.7
5. Install Mahimahi
6. Set up pantheon and run test according to the commands I documented in command_log.pdf
