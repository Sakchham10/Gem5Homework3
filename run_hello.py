import m5
from m5.objects import *

# Create the system
system = System()

# Set the clock frequency
system.clk_domain = SrcClockDmain()
system.clk_domain.clock = '2GHz'
system.clk_domain.voltage_domain = VoltageDomain()

# Enable timing memory mode
system.mem_mode = 'timing'
system.use_virtual_memory = True

# Set the memory range
system.mem_ranges = [AddrRange('512MB')]

# Create a CPU
system.cpu = X86TimingSimpleCPU()

# Configure TLB
system.cpu.itb.size = 128
system.cpu.dtb.size = 128
system.cpu.itb.assoc = 4
system.cpu.dtb.assoc = 4

# Set page size
system.page_size = 4096  # 4KB pages

# Create a memory bus
system.membus = SystemXBar()

# Connect the CPU ports to the membus
system.cpu.icache_port = system.membus.slave
system.cpu.dcache_port = system.membus.slave

# Create a memory controller and connect it to the membus
system.mem_ctrl = DDR3_1600_8x8()
system.mem_ctrl.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.master

# Create a process to run
process = Process()
process.cmd = ['path/to/your/binar']
system.cpu.workload = process
system.cpu.createThreads()

# Instantiate the system and begin execution
root = Root(full_system=False, system=system)
m5.instantiate()

print("Beginning simulation!")
exit_event = m5.simulate()
print('Exiting @ tick {} because {}'
      .format(m5.curTick(), exit_event.getCause()))