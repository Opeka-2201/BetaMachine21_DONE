Arthur LOUIS, S191230
November 18th, 2021

In this submission, you'll find the complete beta machine, a ROM file for control logic and the python script corresponding.

Comments on each block : 

- beta_machine : Using of tunnels to make it clean. Simply connect each component correctly.

- counter_x32 : No comments.

- ALU_x32 : No comments.

- data_memory_x32 : Simple RAM block with always 1 on select to be able to read and write at every moment.

- register_file : No comments.

- control_logic_x32 : To be able to compute the Z value from 1-OR, I create a select bit by comparing the OPCODE with the opcodes of the branching instructions that allows me to pick to good bits for the control logic output.

- intruction_memory_x32 : No comments.

- SEXT : Using a bit extender to take the 16 least significant bits to a 32 bit size (we need to repeat the sign bit to make it correct)

- 1-OR : Simply compares RD1 to 0x0 to compute the value Z used in the control logic for branching instructions.