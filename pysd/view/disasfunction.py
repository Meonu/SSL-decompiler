from capstone import *
from pysd.view.basicblock import bb

class Function:
    def __init__(self,name:str,offset:int):
        self.name:str = name
        self.offset:int = offset
        self.ret_offset = ""
        self.size:int = 0
        self.href:list[str] = []
        self.instructions:list[CsInsn] = []
        self.basic_block:list[bb] = []

    def resolve_symbol_name(self,name:str):
        self.name = name

    def add_href(self,href1):
        self.href.append(href1)

    def add_instruction(self,inst:CsInsn):
        self.instructions.append(inst)
    
    def add_block(self,bb:bb):
        pass

    def set_size(self,size:int):
        self.size = size

    def print_block(self):
        pass