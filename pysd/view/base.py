from abc import ABC, abstractmethod
from pysd.parser.elfparser import ElfParser
from pathlib import Path
from capstone import Cs, CsInsn, CS_ARCH_X86, CS_MODE_32 ,CS_MODE_64
from pysd.linking.linker import resolve_dynamic_linking
from pysd.view.disasfunction import Function

class ViewBase(ABC):

    @classmethod
    def from_file(cls, file: Path):
        return cls(file)

    def __init__(self, file:Path):
        self.parser = ElfParser(file)
        self.dq: dict[int, int] = []
        self.dd: dict[int, ] = {}
        self.disassemble()

    @abstractmethod
    def disasm_entry(self):
        ...

    @abstractmethod
    def disasm_step(self, code: CsInsn) -> bool:
        ...

    def disassemble(self, pop=-1):
        #TODO: 제귀 disassemble 구현
        #! 제귀 disassemble중 함수를 찾으면 function class를 생성하고 disas 한 CsInsn을 function class에 넣어두기
        #! 어떤 함수를 호출했을 때 이미 인식한 함수라면 그 함수에 href 추가하기
        #! disasm_step 을 훅으로 이용할 수 있도록 구현
        pass