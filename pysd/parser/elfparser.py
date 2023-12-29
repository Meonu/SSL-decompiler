from elf import Elf
class ElfParser:
    def parse_section_header(self) -> dict[str,Elf.EndianElf.SectionHeader]:
        secheader_list = self.parse_elf.header.section_headers
        section_headers = {}
        for k in secheader_list:
            if k.name == ".text" :
                section_headers[".text"] = k
            elif k.name == ".plt":
                section_headers[".plt"] = k
            elif k.name == ".symtab":
                section_headers[".symtab"] = k
            elif k.name == ".dynamic":
                section_headers[".dynamic"] = k
            elif k.name == ".dynstr" :
                section_headers[".dynstr"] = k
            elif k.name == ".plt.sec":
                section_headers[".plt.sec"] = k
            elif k.name == ".got.plt":
                section_headers[".got.plt"] = k
            elif k.name == ".strtab":
                section_headers[".strtab"] = k
            if k.name == ".rela.plt" :
                section_headers[".rela.plt"] = k
            elif k.name == ".dynsym":
                section_headers[".dynsym"] = k
        return section_headers

    def resolve_dependencies(self) -> list[str] :
        dependencies = []
        for p in self.section_headers[".dynamic"].body.entries:
            if p.tag == 0x1: #! tag == 0x1 : Needed tag
                str_offset = p.value_or_ptr
                length = 0
                for st in self.section_headers[".dynstr"].body.entries :
                    if length == str_offset:
                        dependencies.append(st)
                        break
                    length += len(st) + 1
        return dependencies


    def __init__(self, filename:str) -> None:
        self.filename:str = filename
        self.parse_elf:Elf = Elf.from_file(filename)
        self.section_headers:dict[str:Elf.EndianElf.SectionHeader] = self.parse_section_header()
        self.entry_point:int = self.parse_elf.header.entry_point
        self.dependencies:list[str] = self.resolve_dependencies()

    def get_entrypoint(self) -> int :
        return self.entry_point

    def get_sectionHeader(self, section_name) -> Elf.EndianElf.SectionHeader:
        return self.section_headers[section_name]

    def get_header(self):
        return self.parse_elf.header

    def get_dependencies(self) -> list[str]:
        return self.dependencies
    
    #오프셋을 입력하면 해당하는 섹션이름을 반환해줌
    def findsection(self, offset:int) -> str:
        for key, value in self.section_headers.items():
            if value.addr <= offset < value.addr + value.len_body:
                return key