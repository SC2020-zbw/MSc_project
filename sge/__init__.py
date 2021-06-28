import subprocess

class job():

    def generate_serial_job_script(name='default',RAM_memory='1G',TMPDIR_memory='15G',hour='0',minute='10',seconds='0',directory=''):
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
            script = script + '#$ -cwd'
        else:
            script = script + '#$ -wd' + directory + '\n'
        # script = script + '#$ -wd /home/' + UCL_id +'/Scratch/workspace' 如果可以就把UCL_id设置为参数

        # Set the working directory to somewhere in your scratch space.  
        #  This is a necessary step as compute nodes cannot write to $HOME.
        # Replace "<your_UCL_id>" with your UCL user ID.
        #$ -wd /home/<your_UCL_id>/Scratch/workspace 好像没有workspace怎么办？
        

        return script

    def generate_script(name='script_name',script=''):

        script_name = str(name) + ".sh"
        f=open(script_name,'w')
        f.write(script)
        f.close()

        return f

    def submit_job(script,email='n'):
        job_message = subprocess.run(['qsub',script],capture_output=True,encoding='utf-8')
        job_ID = job_message.stdout.split()[2]
        return job_ID

    def job_status(job_ID):
        status = subprocess.run(['qstat','-j',job_ID],capture_output=True,encoding='utf-8')
        return status

    
    def delete_job(job_ID):
        info = subprocess.run(['qdel',job_ID],capture_output=True,text=True,shell=True)
        delete_info = info.stdout
        return delete_info