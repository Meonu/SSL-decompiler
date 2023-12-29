from pysd.view.base import ViewBase
from pysd.parser.elf import Elf
from capstone import CsInsn
from pysd.linking.linker import resolve_dynamic_linking

class ElfView(ViewBase) :

    def disasm_entry(self):
        pass
    
    def disasm_step(self, code: CsInsn) -> bool:
        return True