#write a python program Convert Snake case to Pascal case
from string import capwords
import string
string="program_tutorial"
print("Snake case:",string)

Pascal=capwords(string.replace('_',' '))
Pascal=Pascal.replace(' ','')
print("Pascal case:",Pascal)

#Snake case: Program_tutorial
#Pascal case: ProgramTutorial