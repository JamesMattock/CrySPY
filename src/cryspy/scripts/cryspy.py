#!/usr/bin/env python3
'''
Main script
'''

import argparse
import os
import sys

from cryspy.interface import select_code
from cryspy.IO import read_input as rin
from cryspy.start import cryspy_init, cryspy_restart
from cryspy.util.utility import backup_cryspy, clean_cryspy

# ---------- import later
# from cryspy.job.ctrl_ext import Ctrl_ext
# from cryspy.job.ctrl_job import Ctrl_job
# from mpi4py import MPI


def main():
    # ########## MPI start
    # ---------- MPI
    try:
        from mpi4py import MPI
        comm = MPI.COMM_WORLD
        mpi_rank = comm.Get_rank()
        mpi_size = comm.Get_size()
    except Exception as e:
        # ------ if mpi4py is not installed
        comm = None
        mpi_rank = 0
        mpi_size = 1

    # ---------- stdout/stderr
    sys.stdout = open('log_cryspy', 'a')
    sys.stderr = open('err_cryspy', 'a')

    # ---------- argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--backup', help='backup data', action='store_true')
    parser.add_argument('-c', '--clean', help='clean data', action='store_true')
    args = parser.parse_args()

    # ---------- backup option
    if args.backup:
        if mpi_rank == 0:
            backup_cryspy()
        raise SystemExit()

    # ---------- clean option
    if args.clean:
        if mpi_rank == 0:
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
            clean_cryspy()
        raise SystemExit()

    # ---------- lock
    if os.path.isfile('lock_cryspy'):
        if mpi_rank == 0:
            print('lock_cryspy file exists', file=sys.stderr)
        raise SystemExit(1)
    else:
        if mpi_size > 1:
            comm.barrier()
        if mpi_rank == 0:
            with open('lock_cryspy', 'w'):
                pass    # create vacant file
        else:
            pass

    # ---------- initialize
    if not os.path.isfile('cryspy.stat'):
        cryspy_init.initialize(comm, mpi_rank, mpi_size)
        if mpi_rank == 0:
            os.remove('lock_cryspy')
        raise SystemExit()
    # ---------- restart
    else:
        # only stat and init_struc_data in rank0 are important
        stat, init_struc_data = cryspy_restart.restart(comm, mpi_rank, mpi_size)
    # ########## MPI end

    if mpi_rank == 0:
        # ---------- check point 1
        if rin.stop_chkpt == 1:
            print('Stop at check point 1')
            os.remove('lock_cryspy')
            raise SystemExit()

        if not rin.calc_code == 'ext':
            # ---------- check calc files in ./calc_in
            select_code.check_calc_files()
            # ---------- mkdir work/fin
            os.makedirs('work/fin', exist_ok=True)

        # ---------- Perform structure optimization externally
        if rin.calc_code == 'ext':
            # ------ instantiate Ctrl_job class
            from cryspy.job.ctrl_ext import Ctrl_ext
            jobs = Ctrl_ext(stat, init_struc_data)
        # ---------- internally
        else:
            # ---------- instantiate Ctrl_job class
            from cryspy.job.ctrl_job import Ctrl_job
            jobs = Ctrl_job(stat, init_struc_data)

        # ---------- check job status
        jobs.check_job()

        # ---------- handle job
        jobs.handle_job()

        # ---------- recheck for skip and done
        if not rin.calc_code == 'ext':
            if jobs.id_queueing:
                cnt_recheck = 0
                while jobs.recheck:
                    cnt_recheck += 1
                    jobs.recheck = False    # True --> False
                    print('\n\n recheck {}\n'.format(cnt_recheck))
                    jobs.check_job()
                    jobs.handle_job()

        # ---------- next selection or generation
        if not (jobs.id_queueing or jobs.id_running):
            # ---------- next selection or generation
            if rin.algo in ['BO', 'LAQA', 'EA']:
                jobs.next_sg()
            # ---------- for RS
            else:
                print('Done all structures!')

        # ---------- unlock
        os.remove('lock_cryspy')


if __name__ == '__main__':
    # ---------- main
    main()
