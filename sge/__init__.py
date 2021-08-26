'''
The job class representing a Grid Engine job in Python.
Tools for generating script and managing the job.
'''

from os import stat
import subprocess

class job():

    def serial_job_script_code(name='default',RAM_memory='1G',TMPDIR_memory='15G',hour='0',minute='10',seconds='0',directory=''):
        script = '#!/bin/bash -l\n'
        # Batch script to run a serial job under SGE.

        script = script + '#$ -l h_rt=' + str(hour) + ':' + str(minute) + ':' + str(seconds) + '\n'
        #$ -l h_rt=0:10:0
        # Request ten minutes of wallclock time (format hours:minutes:seconds).

        script = script + '#$ -l mem=' + RAM_memory + '\n'
        # Request 1 gigabyte of RAM (must be an integer followed by M, G, or T)
        #$ -l mem=1G

        script = script + '#$ -l tmpfs=' + TMPDIR_memory + '\n'
        # Request 15 gigabyte of TMPDIR space (default is 10 GB - remove if cluster is diskless)
        #$ -l tmpfs=15G

        script = script + '#$ -N ' + name + '\n'
        # Set the name of the job.
        #$ -N Serial_Job

        if (directory==''):
            script = script + '#$ -cwd \n\n'
        else:
            script = script + '#$ -wd' + directory + '\n\n'
        # script = script + '#$ -wd /home/' + UCL_id +'/Scratch/workspace'

        # Set the working directory to somewhere in your scratch space.  
        #  This is a necessary step as compute nodes cannot write to $HOME.
        # Replace "<your_UCL_id>" with your UCL user ID.
        #$ -wd /home/<your_UCL_id>/Scratch/workspace

        return script
    
    def multi_threaded_job_script_code(name='default',RAM_memory='1G',TMPDIR_memory='15G',hour='0',minute='10',seconds='0',directory='',core_num='16'):
        script = job.serial_job_script_code(name,RAM_memory,TMPDIR_memory,hour,minute,seconds,directory)
        
        script = script + '#$ -pe smp ' + core_num + ' \n'
        # Request number of cores.
        
        return script
    
    def mpi_job_script_code(name='default',processes_num='16',RAM_memory='1G',TMPDIR_memory='15G',hour='0',minute='10',seconds='0',directory=''):
        script = job.serial_job_script_code(name,RAM_memory,TMPDIR_memory,hour,minute,seconds,directory)
        
        script = script + '#$ -pe mpi ' + processes_num + ' \n'
        # Select the MPI parallel environment and number of processes.
        
        return script

    # Load module code in script
    def load_module(module_name,script):
        script = script + 'module load ' + module_name + '\n'
        return script

    # Unload module code in script
    def unload_module(module_name,script):
        script = script + 'module unload ' + module_name + '\n'
        return script

    # Add code to run file in script
    def add_working_code(script,run_code):
        script = script + run_code + '\n'
        return script

    # Save the script code into script file
    def generate_script(name='script_name',script=''):

        script_name = str(name) + ".sh"
        f=open(script_name,'w')
        f.write(script)
        f.close()

        return f

    # Submit the job and return the job id
    def submit_job(script_name,email='-n'):
        job_message = subprocess.run(['qsub',script_name],capture_output=True,encoding='utf-8')
        job_ID = job_message.stdout.split()[2]
        return job_ID

    # Check the job status with job id.
    def job_status(job_ID):
        status = subprocess.run(['qstat','-j',job_ID],capture_output=True,shell=True,encoding='utf-8')
        status =status.stdout.strip()
        if status != '': 
            status = status.split('\n')[2].split()[4] 
            if status == 'qw':
                status = 'The job ' + job_ID + ' is queueing and waiting.'
            elif status == 'r':
                status = 'The job ' + job_ID + ' is running.'
            elif status == 't':
                status = 'The job ' + job_ID + ' is being transferred.'
            elif status == 'dr':
                status = 'The job ' + job_ID + ' is being deleted.'
            elif status == 'Rq':
                status = 'A pre-job ' + job_ID + 'check on a node failed and this job was put back in the queue.'
            elif status == 'Rr':
                status = 'The job ' + job_ID + ' was rescheduled but is now running on a new node.'
            elif status == 'Eqw':
                status = 'There was an error in this jobscript ' + job_ID + '. This will not run.'
        else:
            status = 'The job ' + job_ID + ' does not exist.'
        return status


    # Delete the job with corresponding job id
    def delete_job(job_ID):
        if job_ID == 'all':
            info = subprocess.run(['qdel','*'],capture_output=True,encoding='utf-8')
            delete_info = info.stdout.strip()
        else:
            info = subprocess.run(['qdel',job_ID],capture_output=True,encoding='utf-8')
            delete_info = info.stdout.strip()
        return delete_info

    # Read the return output file of job identified by job id.
    def return_output(script_name,job_ID):
        return_output_name = script_name + '.o' + job_ID 
        f=open(return_output_name,'r',encoding='utf-8')
        output = f.read()
        f.close()
        return output

    # Read the return error file of job identified by job id.
    def return_error(script_name,job_ID):
        return_error_name = script_name + '.e' + job_ID
        f=open(return_error_name,'r',encoding='utf-8')
        error = f.read()
        f.close()
        return error