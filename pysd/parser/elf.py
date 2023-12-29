# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Elf(KaitaiStruct):
    """
    .. seealso::
       Source - https://sourceware.org/git/?p=glibc.git;a=blob;f=elf/elf.h;hb=0f62fe0532
    
    
    .. seealso::
       Source - https://refspecs.linuxfoundation.org/elf/gabi4+/contents.html
    
    
    .. seealso::
       Source - https://docs.oracle.com/en/operating-systems/solaris/oracle-solaris/11.4/linkers-libraries/elf-application-binary-interface.html
    """

    class SymbolVisibility(Enum):
        default = 0
        internal = 1
        hidden = 2
        protected = 3
        exported = 4
        singleton = 5
        eliminate = 6

    class SymbolBinding(Enum):
        local = 0
        global_symbol = 1
        weak = 2
        os10 = 10
        os11 = 11
        os12 = 12
        proc13 = 13
        proc14 = 14
        proc15 = 15

    class Endian(Enum):
        le = 1
        be = 2

    class ShType(Enum):
        null_type = 0
        progbits = 1
        symtab = 2
        strtab = 3
        rela = 4
        hash = 5
        dynamic = 6
        note = 7
        nobits = 8
        rel = 9
        shlib = 10
        dynsym = 11
        init_array = 14
        fini_array = 15
        preinit_array = 16
        group = 17
        symtab_shndx = 18
        relr = 19
        sunw_symnsort = 1879048172
        sunw_phname = 1879048173
        sunw_ancillary = 1879048174
        sunw_capchain = 1879048175
        sunw_capinfo = 1879048176
        sunw_symsort = 1879048177
        sunw_tlssort = 1879048178
        sunw_ldynsym = 1879048179
        sunw_dof = 1879048180
        sunw_cap = 1879048181
        sunw_signature = 1879048182
        sunw_annotate = 1879048183
        sunw_debugstr = 1879048184
        sunw_debug = 1879048185
        sunw_move = 1879048186
        sunw_comdat = 1879048187
        sunw_syminfo = 1879048188
        sunw_verdef = 1879048189
        sunw_verneed = 1879048190
        sunw_versym = 1879048191
        sparc_gotdata = 1879048192
        amd64_unwind = 1879048193
        arm_preemptmap = 1879048194
        arm_attributes = 1879048195
        arm_debugoverlay = 1879048196
        arm_overlaysection = 1879048197

    class OsAbi(Enum):
        system_v = 0
        hp_ux = 1
        netbsd = 2
        gnu = 3
        solaris = 6
        aix = 7
        irix = 8
        freebsd = 9
        tru64 = 10
        modesto = 11
        openbsd = 12
        openvms = 13
        nsk = 14
        aros = 15
        fenixos = 16
        cloudabi = 17
        openvos = 18

    class Machine(Enum):
        no_machine = 0
        m32 = 1
        sparc = 2
        x86 = 3
        m68k = 4
        m88k = 5
        iamcu = 6
        i860 = 7
        mips = 8
        s370 = 9
        mips_rs3_le = 10
        parisc = 15
        vpp500 = 17
        sparc32plus = 18
        i960 = 19
        powerpc = 20
        powerpc64 = 21
        s390 = 22
        spu = 23
        v800 = 36
        fr20 = 37
        rh32 = 38
        rce = 39
        arm = 40
        old_alpha = 41
        superh = 42
        sparc_v9 = 43
        tricore = 44
        arc = 45
        h8_300 = 46
        h8_300h = 47
        h8s = 48
        h8_500 = 49
        ia_64 = 50
        mips_x = 51
        coldfire = 52
        m68hc12 = 53
        mma = 54
        pcp = 55
        ncpu = 56
        ndr1 = 57
        starcore = 58
        me16 = 59
        st100 = 60
        tinyj = 61
        x86_64 = 62
        pdsp = 63
        pdp10 = 64
        pdp11 = 65
        fx66 = 66
        st9plus = 67
        st7 = 68
        mc68hc16 = 69
        mc68hc11 = 70
        mc68hc08 = 71
        mc68hc05 = 72
        svx = 73
        st19 = 74
        vax = 75
        cris = 76
        javelin = 77
        firepath = 78
        zsp = 79
        mmix = 80
        huany = 81
        prism = 82
        avr = 83
        fr30 = 84
        d10v = 85
        d30v = 86
        v850 = 87
        m32r = 88
        mn10300 = 89
        mn10200 = 90
        picojava = 91
        openrisc = 92
        arc_compact = 93
        xtensa = 94
        videocore = 95
        tmm_gpp = 96
        ns32k = 97
        tpc = 98
        snp1k = 99
        st200 = 100
        ip2k = 101
        max = 102
        compact_risc = 103
        f2mc16 = 104
        msp430 = 105
        blackfin = 106
        se_c33 = 107
        sep = 108
        arca = 109
        unicore = 110
        excess = 111
        dxp = 112
        altera_nios2 = 113
        crx = 114
        xgate = 115
        c166 = 116
        m16c = 117
        dspic30f = 118
        freescale_ce = 119
        m32c = 120
        tsk3000 = 131
        rs08 = 132
        sharc = 133
        ecog2 = 134
        score7 = 135
        dsp24 = 136
        videocore3 = 137
        latticemico32 = 138
        se_c17 = 139
        ti_c6000 = 140
        ti_c2000 = 141
        ti_c5500 = 142
        ti_arp32 = 143
        ti_pru = 144
        mmdsp_plus = 160
        cypress_m8c = 161
        r32c = 162
        trimedia = 163
        qdsp6 = 164
        i8051 = 165
        stxp7x = 166
        nds32 = 167
        ecog1x = 168
        maxq30 = 169
        ximo16 = 170
        manik = 171
        craynv2 = 172
        rx = 173
        metag = 174
        mcst_elbrus = 175
        ecog16 = 176
        cr16 = 177
        etpu = 178
        sle9x = 179
        l10m = 180
        k10m = 181
        aarch64 = 183
        avr32 = 185
        stm8 = 186
        tile64 = 187
        tilepro = 188
        microblaze = 189
        cuda = 190
        tilegx = 191
        cloudshield = 192
        corea_1st = 193
        corea_2nd = 194
        arcv2 = 195
        open8 = 196
        rl78 = 197
        videocore5 = 198
        renesas_78kor = 199
        freescale_56800ex = 200
        ba1 = 201
        ba2 = 202
        xcore = 203
        mchp_pic = 204
        intelgt = 205
        intel206 = 206
        intel207 = 207
        intel208 = 208
        intel209 = 209
        km32 = 210
        kmx32 = 211
        kmx16 = 212
        kmx8 = 213
        kvarc = 214
        cdp = 215
        coge = 216
        cool = 217
        norc = 218
        csr_kalimba = 219
        z80 = 220
        visium = 221
        ft32 = 222
        moxie = 223
        amd_gpu = 224
        riscv = 243
        lanai = 244
        ceva = 245
        ceva_x2 = 246
        bpf = 247
        graphcore_ipu = 248
        img1 = 249
        nfp = 250
        ve = 251
        csky = 252
        arc_compact3_64 = 253
        mcs6502 = 254
        arc_compact3 = 255
        kvx = 256
        wdc65816 = 257
        loongarch = 258
        kf32 = 259
        u16_u8core = 260
        tachyum = 261
        nxp_56800ef = 262
        avr_old = 4183
        msp430_old = 4185
        adapteva_epiphany = 4643
        mt = 9520
        cygnus_fr30 = 13104
        webassembly = 16727
        xc16x = 18056
        s12z = 19951
        cygnus_frv = 21569
        dlx = 23205
        cygnus_d10v = 30288
        cygnus_d30v = 30326
        ip2k_old = 33303
        cygnus_powerpc = 36901
        alpha = 36902
        cygnus_m32r = 36929
        cygnus_v850 = 36992
        s390_old = 41872
        xtensa_old = 43975
        xstormy16 = 44357
        microblaze_old = 47787
        cygnus_mn10300 = 48879
        cygnus_mn10200 = 57005
        cygnus_mep = 61453
        m32c_old = 65200
        iq2000 = 65210
        nios32 = 65211
        moxie_old = 65261

    class SymbolType(Enum):
        no_type = 0
        object = 1
        func = 2
        section = 3
        file = 4
        common = 5
        tls = 6
        relc = 8
        srelc = 9
        gnu_ifunc = 10
        os11 = 11
        os12 = 12
        proc13 = 13
        proc14 = 14
        proc15 = 15

    class DynamicArrayTags(Enum):
        null = 0
        needed = 1
        pltrelsz = 2
        pltgot = 3
        hash = 4
        strtab = 5
        symtab = 6
        rela = 7
        relasz = 8
        relaent = 9
        strsz = 10
        syment = 11
        init = 12
        fini = 13
        soname = 14
        rpath = 15
        symbolic = 16
        rel = 17
        relsz = 18
        relent = 19
        pltrel = 20
        debug = 21
        textrel = 22
        jmprel = 23
        bind_now = 24
        init_array = 25
        fini_array = 26
        init_arraysz = 27
        fini_arraysz = 28
        runpath = 29
        flags = 30
        preinit_array = 32
        preinit_arraysz = 33
        symtab_shndx = 34
        relrsz = 35
        relr = 36
        relrent = 37
        deprecated_sparc_register = 117440513
        sunw_auxiliary = 1610612749
        sunw_rtldinf = 1610612750
        sunw_filter = 1610612751
        sunw_cap = 1610612752
        sunw_symtab = 1610612753
        sunw_symsz = 1610612754
        sunw_sortent = 1610612755
        sunw_symsort = 1610612756
        sunw_symsortsz = 1610612757
        sunw_tlssort = 1610612758
        sunw_tlssortsz = 1610612759
        sunw_capinfo = 1610612760
        sunw_strpad = 1610612761
        sunw_capchain = 1610612762
        sunw_ldmach = 1610612763
        sunw_symtab_shndx = 1610612764
        sunw_capchainent = 1610612765
        sunw_deferred = 1610612766
        sunw_capchainsz = 1610612767
        sunw_phname = 1610612768
        sunw_parent = 1610612769
        sunw_sx_aslr = 1610612771
        sunw_relax = 1610612773
        sunw_kmod = 1610612775
        sunw_sx_nxheap = 1610612777
        sunw_sx_nxstack = 1610612779
        sunw_sx_adiheap = 1610612781
        sunw_sx_adistack = 1610612783
        sunw_sx_ssbd = 1610612785
        sunw_symnsort = 1610612786
        sunw_symnsortsz = 1610612787
        gnu_flags_1 = 1879047668
        gnu_prelinked = 1879047669
        gnu_conflictsz = 1879047670
        gnu_liblistsz = 1879047671
        checksum = 1879047672
        pltpadsz = 1879047673
        moveent = 1879047674
        movesz = 1879047675
        feature_1 = 1879047676
        posflag_1 = 1879047677
        syminsz = 1879047678
        syminent = 1879047679
        gnu_hash = 1879047925
        tlsdesc_plt = 1879047926
        tlsdesc_got = 1879047927
        gnu_conflict = 1879047928
        gnu_liblist = 1879047929
        config = 1879047930
        depaudit = 1879047931
        audit = 1879047932
        pltpad = 1879047933
        movetab = 1879047934
        syminfo = 1879047935
        versym = 1879048176
        relacount = 1879048185
        relcount = 1879048186
        flags_1 = 1879048187
        verdef = 1879048188
        verdefnum = 1879048189
        verneed = 1879048190
        verneednum = 1879048191
        sparc_register = 1879048193
        auxiliary = 2147483645
        used = 2147483646
        filter = 2147483647

    class Bits(Enum):
        b32 = 1
        b64 = 2

    class PhType(Enum):
        null_type = 0
        load = 1
        dynamic = 2
        interp = 3
        note = 4
        shlib = 5
        phdr = 6
        tls = 7
        gnu_eh_frame = 1685382480
        gnu_stack = 1685382481
        gnu_relro = 1685382482
        gnu_property = 1685382483
        pax_flags = 1694766464
        arm_exidx = 1879048193

    class ObjType(Enum):
        no_file_type = 0
        relocatable = 1
        executable = 2
        shared = 3
        core = 4

    class SectionHeaderIdxSpecial(Enum):
        undefined = 0
        before = 65280
        after = 65281
        amd64_lcommon = 65282
        sunw_ignore = 65343
        abs = 65521
        common = 65522
        xindex = 65535
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\x7F\x45\x4C\x46":
            raise kaitaistruct.ValidationNotEqualError(b"\x7F\x45\x4C\x46", self.magic, self._io, u"/seq/0")
        self.bits = KaitaiStream.resolve_enum(Elf.Bits, self._io.read_u1())
        self.endian = KaitaiStream.resolve_enum(Elf.Endian, self._io.read_u1())
        self.ei_version = self._io.read_u1()
        if not self.ei_version == 1:
            raise kaitaistruct.ValidationNotEqualError(1, self.ei_version, self._io, u"/seq/3")
        self.abi = KaitaiStream.resolve_enum(Elf.OsAbi, self._io.read_u1())
        self.abi_version = self._io.read_u1()
        self.pad = self._io.read_bytes(7)
        if not self.pad == b"\x00\x00\x00\x00\x00\x00\x00":
            raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00", self.pad, self._io, u"/seq/6")
        self.header = Elf.EndianElf(self._io, self, self._root)

    class EndianElf(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            _on = self._root.endian
            if _on == Elf.Endian.le:
                self._is_le = True
            elif _on == Elf.Endian.be:
                self._is_le = False
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/endian_elf")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self.e_type = KaitaiStream.resolve_enum(Elf.ObjType, self._io.read_u2le())
            self.machine = KaitaiStream.resolve_enum(Elf.Machine, self._io.read_u2le())
            self.e_version = self._io.read_u4le()
            _on = self._root.bits
            if _on == Elf.Bits.b32:
                self.entry_point = self._io.read_u4le()
            elif _on == Elf.Bits.b64:
                self.entry_point = self._io.read_u8le()
            _on = self._root.bits
            if _on == Elf.Bits.b32:
                self.program_header_offset = self._io.read_u4le()
            elif _on == Elf.Bits.b64:
                self.program_header_offset = self._io.read_u8le()
            _on = self._root.bits
            if _on == Elf.Bits.b32:
                self.section_header_offset = self._io.read_u4le()
            elif _on == Elf.Bits.b64:
                self.section_header_offset = self._io.read_u8le()
            self.flags = self._io.read_bytes(4)
            self.e_ehsize = self._io.read_u2le()
            self.len_program_headers = self._io.read_u2le()
            self.num_program_headers = self._io.read_u2le()
            self.len_section_headers = self._io.read_u2le()
            self.num_section_headers = self._io.read_u2le()
            self.section_names_idx = self._io.read_u2le()

        def _read_be(self):
            self.e_type = KaitaiStream.resolve_enum(Elf.ObjType, self._io.read_u2be())
            self.machine = KaitaiStream.resolve_enum(Elf.Machine, self._io.read_u2be())
            self.e_version = self._io.read_u4be()
            _on = self._root.bits
            if _on == Elf.Bits.b32:
                self.entry_point = self._io.read_u4be()
            elif _on == Elf.Bits.b64:
                self.entry_point = self._io.read_u8be()
            _on = self._root.bits
            if _on == Elf.Bits.b32:
                self.program_header_offset = self._io.read_u4be()
            elif _on == Elf.Bits.b64:
                self.program_header_offset = self._io.read_u8be()
            _on = self._root.bits
            if _on == Elf.Bits.b32:
                self.section_header_offset = self._io.read_u4be()
            elif _on == Elf.Bits.b64:
                self.section_header_offset = self._io.read_u8be()
            self.flags = self._io.read_bytes(4)
            self.e_ehsize = self._io.read_u2be()
            self.len_program_headers = self._io.read_u2be()
            self.num_program_headers = self._io.read_u2be()
            self.len_section_headers = self._io.read_u2be()
            self.num_section_headers = self._io.read_u2be()
            self.section_names_idx = self._io.read_u2be()

        class NoteSection(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/endian_elf/types/note_section")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self.entries = []
                i = 0
                while not self._io.is_eof():
                    self.entries.append(Elf.EndianElf.NoteSectionEntry(self._io, self, self._root, self._is_le))
                    i += 1


            def _read_be(self):
                self.entries = []
                i = 0
                while not self._io.is_eof():
                    self.entries.append(Elf.EndianElf.NoteSectionEntry(self._io, self, self._root, self._is_le))
                    i += 1



        class ProgramHeader(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/endian_elf/types/program_header")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self.type = KaitaiStream.resolve_enum(Elf.PhType, self._io.read_u4le())
                if self._root.bits == Elf.Bits.b64:
                    self.flags64 = self._io.read_u4le()

                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.offset = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.offset = self._io.read_u8le()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.vaddr = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.vaddr = self._io.read_u8le()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.paddr = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.paddr = self._io.read_u8le()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.filesz = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.filesz = self._io.read_u8le()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.memsz = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.memsz = self._io.read_u8le()
                if self._root.bits == Elf.Bits.b32:
                    self.flags32 = self._io.read_u4le()

                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.align = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.align = self._io.read_u8le()

            def _read_be(self):
                self.type = KaitaiStream.resolve_enum(Elf.PhType, self._io.read_u4be())
                if self._root.bits == Elf.Bits.b64:
                    self.flags64 = self._io.read_u4be()

                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.offset = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.offset = self._io.read_u8be()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.vaddr = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.vaddr = self._io.read_u8be()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.paddr = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.paddr = self._io.read_u8be()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.filesz = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.filesz = self._io.read_u8be()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.memsz = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.memsz = self._io.read_u8be()
                if self._root.bits == Elf.Bits.b32:
                    self.flags32 = self._io.read_u4be()

                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.align = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.align = self._io.read_u8be()

            @property
            def flags_obj(self):
                if hasattr(self, '_m_flags_obj'):
                    return self._m_flags_obj

                if self._is_le:
                    _on = self._root.bits
                    if _on == Elf.Bits.b32:
                        self._m_flags_obj = Elf.PhdrTypeFlags(self.flags32, self._io, self, self._root)
                    elif _on == Elf.Bits.b64:
                        self._m_flags_obj = Elf.PhdrTypeFlags(self.flags64, self._io, self, self._root)
                else:
                    _on = self._root.bits
                    if _on == Elf.Bits.b32:
                        self._m_flags_obj = Elf.PhdrTypeFlags(self.flags32, self._io, self, self._root)
                    elif _on == Elf.Bits.b64:
                        self._m_flags_obj = Elf.PhdrTypeFlags(self.flags64, self._io, self, self._root)
                return getattr(self, '_m_flags_obj', None)


        class DynamicSectionEntry(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/en/operating-systems/solaris/oracle-solaris/11.4/linkers-libraries/dynamic-section.html
            
            
            .. seealso::
               Source - https://refspecs.linuxfoundation.org/elf/gabi4+/ch5.dynamic.html#dynamic_section
            """
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/endian_elf/types/dynamic_section_entry")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.tag = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.tag = self._io.read_u8le()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.value_or_ptr = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.value_or_ptr = self._io.read_u8le()

            def _read_be(self):
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.tag = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.tag = self._io.read_u8be()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.value_or_ptr = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.value_or_ptr = self._io.read_u8be()

            @property
            def flag_1_values(self):
                if hasattr(self, '_m_flag_1_values'):
                    return self._m_flag_1_values

                if self.tag_enum == Elf.DynamicArrayTags.flags_1:
                    if self._is_le:
                        self._m_flag_1_values = Elf.DtFlag1Values(self.value_or_ptr, self._io, self, self._root)
                    else:
                        self._m_flag_1_values = Elf.DtFlag1Values(self.value_or_ptr, self._io, self, self._root)

                return getattr(self, '_m_flag_1_values', None)

            @property
            def value_str(self):
                if hasattr(self, '_m_value_str'):
                    return self._m_value_str

                if  ((self.is_value_str) and (self._parent.is_string_table_linked)) :
                    io = self._parent._parent.linked_section.body._io
                    _pos = io.pos()
                    io.seek(self.value_or_ptr)
                    if self._is_le:
                        self._m_value_str = (io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
                    else:
                        self._m_value_str = (io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
                    io.seek(_pos)

                return getattr(self, '_m_value_str', None)

            @property
            def tag_enum(self):
                if hasattr(self, '_m_tag_enum'):
                    return self._m_tag_enum

                self._m_tag_enum = KaitaiStream.resolve_enum(Elf.DynamicArrayTags, self.tag)
                return getattr(self, '_m_tag_enum', None)

            @property
            def flag_values(self):
                if hasattr(self, '_m_flag_values'):
                    return self._m_flag_values

                if self.tag_enum == Elf.DynamicArrayTags.flags:
                    if self._is_le:
                        self._m_flag_values = Elf.DtFlagValues(self.value_or_ptr, self._io, self, self._root)
                    else:
                        self._m_flag_values = Elf.DtFlagValues(self.value_or_ptr, self._io, self, self._root)

                return getattr(self, '_m_flag_values', None)

            @property
            def is_value_str(self):
                if hasattr(self, '_m_is_value_str'):
                    return self._m_is_value_str

                self._m_is_value_str =  ((self.value_or_ptr != 0) and ( ((self.tag_enum == Elf.DynamicArrayTags.needed) or (self.tag_enum == Elf.DynamicArrayTags.soname) or (self.tag_enum == Elf.DynamicArrayTags.rpath) or (self.tag_enum == Elf.DynamicArrayTags.runpath) or (self.tag_enum == Elf.DynamicArrayTags.sunw_auxiliary) or (self.tag_enum == Elf.DynamicArrayTags.sunw_filter) or (self.tag_enum == Elf.DynamicArrayTags.auxiliary) or (self.tag_enum == Elf.DynamicArrayTags.filter) or (self.tag_enum == Elf.DynamicArrayTags.config) or (self.tag_enum == Elf.DynamicArrayTags.depaudit) or (self.tag_enum == Elf.DynamicArrayTags.audit)) )) 
                return getattr(self, '_m_is_value_str', None)


        class SectionHeader(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/endian_elf/types/section_header")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self.ofs_name = self._io.read_u4le()
                self.type = KaitaiStream.resolve_enum(Elf.ShType, self._io.read_u4le())
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.flags = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.flags = self._io.read_u8le()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.addr = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.addr = self._io.read_u8le()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.ofs_body = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.ofs_body = self._io.read_u8le()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.len_body = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.len_body = self._io.read_u8le()
                self.linked_section_idx = self._io.read_u4le()
                self.info = self._io.read_bytes(4)
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.align = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.align = self._io.read_u8le()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.entry_size = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.entry_size = self._io.read_u8le()

            def _read_be(self):
                self.ofs_name = self._io.read_u4be()
                self.type = KaitaiStream.resolve_enum(Elf.ShType, self._io.read_u4be())
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.flags = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.flags = self._io.read_u8be()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.addr = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.addr = self._io.read_u8be()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.ofs_body = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.ofs_body = self._io.read_u8be()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.len_body = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.len_body = self._io.read_u8be()
                self.linked_section_idx = self._io.read_u4be()
                self.info = self._io.read_bytes(4)
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.align = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.align = self._io.read_u8be()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.entry_size = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.entry_size = self._io.read_u8be()

            @property
            def body(self):
                if hasattr(self, '_m_body'):
                    return self._m_body

                if self.type != Elf.ShType.nobits:
                    io = self._root._io
                    _pos = io.pos()
                    io.seek(self.ofs_body)
                    if self._is_le:
                        _on = self.type
                        if _on == Elf.ShType.rel:
                            self._raw__m_body = io.read_bytes(self.len_body)
                            _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                            self._m_body = Elf.EndianElf.RelocationSection(False, _io__raw__m_body, self, self._root, self._is_le)
                        elif _on == Elf.ShType.note:
                            self._raw__m_body = io.read_bytes(self.len_body)
                            _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                            self._m_body = Elf.EndianElf.NoteSection(_io__raw__m_body, self, self._root, self._is_le)
                        elif _on == Elf.ShType.symtab:
                            self._raw__m_body = io.read_bytes(self.len_body)
                            _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                            self._m_body = Elf.EndianElf.DynsymSection(_io__raw__m_body, self, self._root, self._is_le)
                        elif _on == Elf.ShType.strtab:
                            self._raw__m_body = io.read_bytes(self.len_body)
                            _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                            self._m_body = Elf.EndianElf.StringsStruct(_io__raw__m_body, self, self._root, self._is_le)
                        elif _on == Elf.ShType.dynamic:
                            self._raw__m_body = io.read_bytes(self.len_body)
                            _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                            self._m_body = Elf.EndianElf.DynamicSection(_io__raw__m_body, self, self._root, self._is_le)
                        elif _on == Elf.ShType.dynsym:
                            self._raw__m_body = io.read_bytes(self.len_body)
                            _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                            self._m_body = Elf.EndianElf.DynsymSection(_io__raw__m_body, self, self._root, self._is_le)
                        elif _on == Elf.ShType.rela:
                            self._raw__m_body = io.read_bytes(self.len_body)
                            _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                            self._m_body = Elf.EndianElf.RelocationSection(True, _io__raw__m_body, self, self._root, self._is_le)
                        else:
                            self._m_body = io.read_bytes(self.len_body)
                    else:
                        _on = self.type
                        if _on == Elf.ShType.rel:
                            self._raw__m_body = io.read_bytes(self.len_body)
                            _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                            self._m_body = Elf.EndianElf.RelocationSection(False, _io__raw__m_body, self, self._root, self._is_le)
                        elif _on == Elf.ShType.note:
                            self._raw__m_body = io.read_bytes(self.len_body)
                            _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                            self._m_body = Elf.EndianElf.NoteSection(_io__raw__m_body, self, self._root, self._is_le)
                        elif _on == Elf.ShType.symtab:
                            self._raw__m_body = io.read_bytes(self.len_body)
                            _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                            self._m_body = Elf.EndianElf.DynsymSection(_io__raw__m_body, self, self._root, self._is_le)
                        elif _on == Elf.ShType.strtab:
                            self._raw__m_body = io.read_bytes(self.len_body)
                            _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                            self._m_body = Elf.EndianElf.StringsStruct(_io__raw__m_body, self, self._root, self._is_le)
                        elif _on == Elf.ShType.dynamic:
                            self._raw__m_body = io.read_bytes(self.len_body)
                            _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                            self._m_body = Elf.EndianElf.DynamicSection(_io__raw__m_body, self, self._root, self._is_le)
                        elif _on == Elf.ShType.dynsym:
                            self._raw__m_body = io.read_bytes(self.len_body)
                            _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                            self._m_body = Elf.EndianElf.DynsymSection(_io__raw__m_body, self, self._root, self._is_le)
                        elif _on == Elf.ShType.rela:
                            self._raw__m_body = io.read_bytes(self.len_body)
                            _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                            self._m_body = Elf.EndianElf.RelocationSection(True, _io__raw__m_body, self, self._root, self._is_le)
                        else:
                            self._m_body = io.read_bytes(self.len_body)
                    io.seek(_pos)

                return getattr(self, '_m_body', None)

            @property
            def linked_section(self):
                """may reference a later section header, so don't try to access too early (use only lazy `instances`).
                
                .. seealso::
                   Source - https://refspecs.linuxfoundation.org/elf/gabi4+/ch4.sheader.html#sh_link
                """
                if hasattr(self, '_m_linked_section'):
                    return self._m_linked_section

                if  ((self.linked_section_idx != Elf.SectionHeaderIdxSpecial.undefined.value) and (self.linked_section_idx < self._root.header.num_section_headers)) :
                    self._m_linked_section = self._root.header.section_headers[self.linked_section_idx]

                return getattr(self, '_m_linked_section', None)

            @property
            def name(self):
                if hasattr(self, '_m_name'):
                    return self._m_name

                io = self._root.header.section_names._io
                _pos = io.pos()
                io.seek(self.ofs_name)
                if self._is_le:
                    self._m_name = (io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
                else:
                    self._m_name = (io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
                io.seek(_pos)
                return getattr(self, '_m_name', None)

            @property
            def flags_obj(self):
                if hasattr(self, '_m_flags_obj'):
                    return self._m_flags_obj

                if self._is_le:
                    self._m_flags_obj = Elf.SectionHeaderFlags(self.flags, self._io, self, self._root)
                else:
                    self._m_flags_obj = Elf.SectionHeaderFlags(self.flags, self._io, self, self._root)
                return getattr(self, '_m_flags_obj', None)


        class RelocationSection(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/en/operating-systems/solaris/oracle-solaris/11.4/linkers-libraries/relocation-sections.html
            
            
            .. seealso::
               Source - https://refspecs.linuxfoundation.org/elf/gabi4+/ch4.reloc.html
            """
            def __init__(self, has_addend, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le
                self.has_addend = has_addend
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/endian_elf/types/relocation_section")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self.entries = []
                i = 0
                while not self._io.is_eof():
                    self.entries.append(Elf.EndianElf.RelocationSectionEntry(self._io, self, self._root, self._is_le))
                    i += 1


            def _read_be(self):
                self.entries = []
                i = 0
                while not self._io.is_eof():
                    self.entries.append(Elf.EndianElf.RelocationSectionEntry(self._io, self, self._root, self._is_le))
                    i += 1



        class DynamicSection(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/endian_elf/types/dynamic_section")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self.entries = []
                i = 0
                while not self._io.is_eof():
                    self.entries.append(Elf.EndianElf.DynamicSectionEntry(self._io, self, self._root, self._is_le))
                    i += 1


            def _read_be(self):
                self.entries = []
                i = 0
                while not self._io.is_eof():
                    self.entries.append(Elf.EndianElf.DynamicSectionEntry(self._io, self, self._root, self._is_le))
                    i += 1


            @property
            def is_string_table_linked(self):
                if hasattr(self, '_m_is_string_table_linked'):
                    return self._m_is_string_table_linked

                self._m_is_string_table_linked = self._parent.linked_section.type == Elf.ShType.strtab
                return getattr(self, '_m_is_string_table_linked', None)


        class DynsymSection(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/endian_elf/types/dynsym_section")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self.entries = []
                i = 0
                while not self._io.is_eof():
                    self.entries.append(Elf.EndianElf.DynsymSectionEntry(self._io, self, self._root, self._is_le))
                    i += 1


            def _read_be(self):
                self.entries = []
                i = 0
                while not self._io.is_eof():
                    self.entries.append(Elf.EndianElf.DynsymSectionEntry(self._io, self, self._root, self._is_le))
                    i += 1


            @property
            def is_string_table_linked(self):
                if hasattr(self, '_m_is_string_table_linked'):
                    return self._m_is_string_table_linked

                self._m_is_string_table_linked = self._parent.linked_section.type == Elf.ShType.strtab
                return getattr(self, '_m_is_string_table_linked', None)


        class RelocationSectionEntry(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/endian_elf/types/relocation_section_entry")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.offset = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.offset = self._io.read_u8le()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.info = self._io.read_u4le()
                elif _on == Elf.Bits.b64:
                    self.info = self._io.read_u8le()
                if self._parent.has_addend:
                    _on = self._root.bits
                    if _on == Elf.Bits.b32:
                        self.addend = self._io.read_s4le()
                    elif _on == Elf.Bits.b64:
                        self.addend = self._io.read_s8le()


            def _read_be(self):
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.offset = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.offset = self._io.read_u8be()
                _on = self._root.bits
                if _on == Elf.Bits.b32:
                    self.info = self._io.read_u4be()
                elif _on == Elf.Bits.b64:
                    self.info = self._io.read_u8be()
                if self._parent.has_addend:
                    _on = self._root.bits
                    if _on == Elf.Bits.b32:
                        self.addend = self._io.read_s4be()
                    elif _on == Elf.Bits.b64:
                        self.addend = self._io.read_s8be()



        class DynsymSectionEntry(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/en/operating-systems/solaris/oracle-solaris/11.4/linkers-libraries/symbol-table-section.html
            
            
            .. seealso::
               Source - https://refspecs.linuxfoundation.org/elf/gabi4+/ch4.symtab.html
            """
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/endian_elf/types/dynsym_section_entry")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self.ofs_name = self._io.read_u4le()
                if self._root.bits == Elf.Bits.b32:
                    self.value_b32 = self._io.read_u4le()

                if self._root.bits == Elf.Bits.b32:
                    self.size_b32 = self._io.read_u4le()

                self.bind = KaitaiStream.resolve_enum(Elf.SymbolBinding, self._io.read_bits_int_be(4))
                self.type = KaitaiStream.resolve_enum(Elf.SymbolType, self._io.read_bits_int_be(4))
                self._io.align_to_byte()
                self.other = self._io.read_u1()
                self.sh_idx = self._io.read_u2le()
                if self._root.bits == Elf.Bits.b64:
                    self.value_b64 = self._io.read_u8le()

                if self._root.bits == Elf.Bits.b64:
                    self.size_b64 = self._io.read_u8le()


            def _read_be(self):
                self.ofs_name = self._io.read_u4be()
                if self._root.bits == Elf.Bits.b32:
                    self.value_b32 = self._io.read_u4be()

                if self._root.bits == Elf.Bits.b32:
                    self.size_b32 = self._io.read_u4be()

                self.bind = KaitaiStream.resolve_enum(Elf.SymbolBinding, self._io.read_bits_int_be(4))
                self.type = KaitaiStream.resolve_enum(Elf.SymbolType, self._io.read_bits_int_be(4))
                self._io.align_to_byte()
                self.other = self._io.read_u1()
                self.sh_idx = self._io.read_u2be()
                if self._root.bits == Elf.Bits.b64:
                    self.value_b64 = self._io.read_u8be()

                if self._root.bits == Elf.Bits.b64:
                    self.size_b64 = self._io.read_u8be()


            @property
            def is_sh_idx_reserved(self):
                if hasattr(self, '_m_is_sh_idx_reserved'):
                    return self._m_is_sh_idx_reserved

                self._m_is_sh_idx_reserved =  ((self.sh_idx >= self._root.sh_idx_lo_reserved) and (self.sh_idx <= self._root.sh_idx_hi_reserved)) 
                return getattr(self, '_m_is_sh_idx_reserved', None)

            @property
            def is_sh_idx_os(self):
                if hasattr(self, '_m_is_sh_idx_os'):
                    return self._m_is_sh_idx_os

                self._m_is_sh_idx_os =  ((self.sh_idx >= self._root.sh_idx_lo_os) and (self.sh_idx <= self._root.sh_idx_hi_os)) 
                return getattr(self, '_m_is_sh_idx_os', None)

            @property
            def is_sh_idx_proc(self):
                if hasattr(self, '_m_is_sh_idx_proc'):
                    return self._m_is_sh_idx_proc

                self._m_is_sh_idx_proc =  ((self.sh_idx >= self._root.sh_idx_lo_proc) and (self.sh_idx <= self._root.sh_idx_hi_proc)) 
                return getattr(self, '_m_is_sh_idx_proc', None)

            @property
            def size(self):
                if hasattr(self, '_m_size'):
                    return self._m_size

                self._m_size = (self.size_b32 if self._root.bits == Elf.Bits.b32 else (self.size_b64 if self._root.bits == Elf.Bits.b64 else 0))
                return getattr(self, '_m_size', None)

            @property
            def visibility(self):
                if hasattr(self, '_m_visibility'):
                    return self._m_visibility

                self._m_visibility = KaitaiStream.resolve_enum(Elf.SymbolVisibility, (self.other & 3))
                return getattr(self, '_m_visibility', None)

            @property
            def value(self):
                if hasattr(self, '_m_value'):
                    return self._m_value

                self._m_value = (self.value_b32 if self._root.bits == Elf.Bits.b32 else (self.value_b64 if self._root.bits == Elf.Bits.b64 else 0))
                return getattr(self, '_m_value', None)

            @property
            def name(self):
                if hasattr(self, '_m_name'):
                    return self._m_name

                if  ((self.ofs_name != 0) and (self._parent.is_string_table_linked)) :
                    io = self._parent._parent.linked_section.body._io
                    _pos = io.pos()
                    io.seek(self.ofs_name)
                    if self._is_le:
                        self._m_name = (io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
                    else:
                        self._m_name = (io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
                    io.seek(_pos)

                return getattr(self, '_m_name', None)

            @property
            def sh_idx_special(self):
                if hasattr(self, '_m_sh_idx_special'):
                    return self._m_sh_idx_special

                self._m_sh_idx_special = KaitaiStream.resolve_enum(Elf.SectionHeaderIdxSpecial, self.sh_idx)
                return getattr(self, '_m_sh_idx_special', None)


        class NoteSectionEntry(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/en/operating-systems/solaris/oracle-solaris/11.4/linkers-libraries/note-section.html
            
            
            .. seealso::
               Source - https://refspecs.linuxfoundation.org/elf/gabi4+/ch5.pheader.html#note_section
            """
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/endian_elf/types/note_section_entry")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self.len_name = self._io.read_u4le()
                self.len_descriptor = self._io.read_u4le()
                self.type = self._io.read_u4le()
                self.name = KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_name), 0, False)
                self.name_padding = self._io.read_bytes((-(self.len_name) % 4))
                self.descriptor = self._io.read_bytes(self.len_descriptor)
                self.descriptor_padding = self._io.read_bytes((-(self.len_descriptor) % 4))

            def _read_be(self):
                self.len_name = self._io.read_u4be()
                self.len_descriptor = self._io.read_u4be()
                self.type = self._io.read_u4be()
                self.name = KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_name), 0, False)
                self.name_padding = self._io.read_bytes((-(self.len_name) % 4))
                self.descriptor = self._io.read_bytes(self.len_descriptor)
                self.descriptor_padding = self._io.read_bytes((-(self.len_descriptor) % 4))


        class StringsStruct(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/endian_elf/types/strings_struct")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self.entries = []
                i = 0
                while not self._io.is_eof():
                    self.entries.append((self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8"))
                    i += 1


            def _read_be(self):
                self.entries = []
                i = 0
                while not self._io.is_eof():
                    self.entries.append((self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8"))
                    i += 1



        @property
        def program_headers(self):
            if hasattr(self, '_m_program_headers'):
                return self._m_program_headers

            _pos = self._io.pos()
            self._io.seek(self.program_header_offset)
            if self._is_le:
                self._raw__m_program_headers = []
                self._m_program_headers = []
                for i in range(self.num_program_headers):
                    self._raw__m_program_headers.append(self._io.read_bytes(self.len_program_headers))
                    _io__raw__m_program_headers = KaitaiStream(BytesIO(self._raw__m_program_headers[i]))
                    self._m_program_headers.append(Elf.EndianElf.ProgramHeader(_io__raw__m_program_headers, self, self._root, self._is_le))

            else:
                self._raw__m_program_headers = []
                self._m_program_headers = []
                for i in range(self.num_program_headers):
                    self._raw__m_program_headers.append(self._io.read_bytes(self.len_program_headers))
                    _io__raw__m_program_headers = KaitaiStream(BytesIO(self._raw__m_program_headers[i]))
                    self._m_program_headers.append(Elf.EndianElf.ProgramHeader(_io__raw__m_program_headers, self, self._root, self._is_le))

            self._io.seek(_pos)
            return getattr(self, '_m_program_headers', None)

        @property
        def section_headers(self):
            if hasattr(self, '_m_section_headers'):
                return self._m_section_headers

            _pos = self._io.pos()
            self._io.seek(self.section_header_offset)
            if self._is_le:
                self._raw__m_section_headers = []
                self._m_section_headers = []
                for i in range(self.num_section_headers):
                    self._raw__m_section_headers.append(self._io.read_bytes(self.len_section_headers))
                    _io__raw__m_section_headers = KaitaiStream(BytesIO(self._raw__m_section_headers[i]))
                    self._m_section_headers.append(Elf.EndianElf.SectionHeader(_io__raw__m_section_headers, self, self._root, self._is_le))

            else:
                self._raw__m_section_headers = []
                self._m_section_headers = []
                for i in range(self.num_section_headers):
                    self._raw__m_section_headers.append(self._io.read_bytes(self.len_section_headers))
                    _io__raw__m_section_headers = KaitaiStream(BytesIO(self._raw__m_section_headers[i]))
                    self._m_section_headers.append(Elf.EndianElf.SectionHeader(_io__raw__m_section_headers, self, self._root, self._is_le))

            self._io.seek(_pos)
            return getattr(self, '_m_section_headers', None)

        @property
        def section_names(self):
            if hasattr(self, '_m_section_names'):
                return self._m_section_names

            if  ((self.section_names_idx != Elf.SectionHeaderIdxSpecial.undefined.value) and (self.section_names_idx < self._root.header.num_section_headers)) :
                _pos = self._io.pos()
                self._io.seek(self.section_headers[self.section_names_idx].ofs_body)
                if self._is_le:
                    self._raw__m_section_names = self._io.read_bytes(self.section_headers[self.section_names_idx].len_body)
                    _io__raw__m_section_names = KaitaiStream(BytesIO(self._raw__m_section_names))
                    self._m_section_names = Elf.EndianElf.StringsStruct(_io__raw__m_section_names, self, self._root, self._is_le)
                else:
                    self._raw__m_section_names = self._io.read_bytes(self.section_headers[self.section_names_idx].len_body)
                    _io__raw__m_section_names = KaitaiStream(BytesIO(self._raw__m_section_names))
                    self._m_section_names = Elf.EndianElf.StringsStruct(_io__raw__m_section_names, self, self._root, self._is_le)
                self._io.seek(_pos)

            return getattr(self, '_m_section_names', None)


    class DtFlag1Values(KaitaiStruct):
        def __init__(self, value, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.value = value
            self._read()

        def _read(self):
            pass

        @property
        def singleton(self):
            """Singleton symbols are used."""
            if hasattr(self, '_m_singleton'):
                return self._m_singleton

            self._m_singleton = (self.value & 33554432) != 0
            return getattr(self, '_m_singleton', None)

        @property
        def ignmuldef(self):
            if hasattr(self, '_m_ignmuldef'):
                return self._m_ignmuldef

            self._m_ignmuldef = (self.value & 262144) != 0
            return getattr(self, '_m_ignmuldef', None)

        @property
        def loadfltr(self):
            """Trigger filtee loading at runtime."""
            if hasattr(self, '_m_loadfltr'):
                return self._m_loadfltr

            self._m_loadfltr = (self.value & 16) != 0
            return getattr(self, '_m_loadfltr', None)

        @property
        def initfirst(self):
            """Set RTLD_INITFIRST for this object."""
            if hasattr(self, '_m_initfirst'):
                return self._m_initfirst

            self._m_initfirst = (self.value & 32) != 0
            return getattr(self, '_m_initfirst', None)

        @property
        def symintpose(self):
            """Object has individual interposers."""
            if hasattr(self, '_m_symintpose'):
                return self._m_symintpose

            self._m_symintpose = (self.value & 8388608) != 0
            return getattr(self, '_m_symintpose', None)

        @property
        def noreloc(self):
            if hasattr(self, '_m_noreloc'):
                return self._m_noreloc

            self._m_noreloc = (self.value & 4194304) != 0
            return getattr(self, '_m_noreloc', None)

        @property
        def confalt(self):
            """Configuration alternative created."""
            if hasattr(self, '_m_confalt'):
                return self._m_confalt

            self._m_confalt = (self.value & 8192) != 0
            return getattr(self, '_m_confalt', None)

        @property
        def dispreldne(self):
            """Disp reloc applied at build time."""
            if hasattr(self, '_m_dispreldne'):
                return self._m_dispreldne

            self._m_dispreldne = (self.value & 32768) != 0
            return getattr(self, '_m_dispreldne', None)

        @property
        def rtld_global(self):
            """Set RTLD_GLOBAL for this object."""
            if hasattr(self, '_m_rtld_global'):
                return self._m_rtld_global

            self._m_rtld_global = (self.value & 2) != 0
            return getattr(self, '_m_rtld_global', None)

        @property
        def nodelete(self):
            """Set RTLD_NODELETE for this object."""
            if hasattr(self, '_m_nodelete'):
                return self._m_nodelete

            self._m_nodelete = (self.value & 8) != 0
            return getattr(self, '_m_nodelete', None)

        @property
        def trans(self):
            if hasattr(self, '_m_trans'):
                return self._m_trans

            self._m_trans = (self.value & 512) != 0
            return getattr(self, '_m_trans', None)

        @property
        def origin(self):
            """$ORIGIN must be handled."""
            if hasattr(self, '_m_origin'):
                return self._m_origin

            self._m_origin = (self.value & 128) != 0
            return getattr(self, '_m_origin', None)

        @property
        def now(self):
            """Set RTLD_NOW for this object."""
            if hasattr(self, '_m_now'):
                return self._m_now

            self._m_now = (self.value & 1) != 0
            return getattr(self, '_m_now', None)

        @property
        def nohdr(self):
            if hasattr(self, '_m_nohdr'):
                return self._m_nohdr

            self._m_nohdr = (self.value & 1048576) != 0
            return getattr(self, '_m_nohdr', None)

        @property
        def endfiltee(self):
            """Filtee terminates filters search."""
            if hasattr(self, '_m_endfiltee'):
                return self._m_endfiltee

            self._m_endfiltee = (self.value & 16384) != 0
            return getattr(self, '_m_endfiltee', None)

        @property
        def nodirect(self):
            """Object has no-direct binding."""
            if hasattr(self, '_m_nodirect'):
                return self._m_nodirect

            self._m_nodirect = (self.value & 131072) != 0
            return getattr(self, '_m_nodirect', None)

        @property
        def globaudit(self):
            """Global auditing required."""
            if hasattr(self, '_m_globaudit'):
                return self._m_globaudit

            self._m_globaudit = (self.value & 16777216) != 0
            return getattr(self, '_m_globaudit', None)

        @property
        def noksyms(self):
            if hasattr(self, '_m_noksyms'):
                return self._m_noksyms

            self._m_noksyms = (self.value & 524288) != 0
            return getattr(self, '_m_noksyms', None)

        @property
        def interpose(self):
            """Object is used to interpose."""
            if hasattr(self, '_m_interpose'):
                return self._m_interpose

            self._m_interpose = (self.value & 1024) != 0
            return getattr(self, '_m_interpose', None)

        @property
        def nodump(self):
            """Object can't be dldump'ed."""
            if hasattr(self, '_m_nodump'):
                return self._m_nodump

            self._m_nodump = (self.value & 4096) != 0
            return getattr(self, '_m_nodump', None)

        @property
        def disprelpnd(self):
            """Disp reloc applied at run-time."""
            if hasattr(self, '_m_disprelpnd'):
                return self._m_disprelpnd

            self._m_disprelpnd = (self.value & 65536) != 0
            return getattr(self, '_m_disprelpnd', None)

        @property
        def noopen(self):
            """Set RTLD_NOOPEN for this object."""
            if hasattr(self, '_m_noopen'):
                return self._m_noopen

            self._m_noopen = (self.value & 64) != 0
            return getattr(self, '_m_noopen', None)

        @property
        def stub(self):
            if hasattr(self, '_m_stub'):
                return self._m_stub

            self._m_stub = (self.value & 67108864) != 0
            return getattr(self, '_m_stub', None)

        @property
        def direct(self):
            """Direct binding enabled."""
            if hasattr(self, '_m_direct'):
                return self._m_direct

            self._m_direct = (self.value & 256) != 0
            return getattr(self, '_m_direct', None)

        @property
        def edited(self):
            """Object is modified after built."""
            if hasattr(self, '_m_edited'):
                return self._m_edited

            self._m_edited = (self.value & 2097152) != 0
            return getattr(self, '_m_edited', None)

        @property
        def group(self):
            """Set RTLD_GROUP for this object."""
            if hasattr(self, '_m_group'):
                return self._m_group

            self._m_group = (self.value & 4) != 0
            return getattr(self, '_m_group', None)

        @property
        def pie(self):
            if hasattr(self, '_m_pie'):
                return self._m_pie

            self._m_pie = (self.value & 134217728) != 0
            return getattr(self, '_m_pie', None)

        @property
        def nodeflib(self):
            """Ignore default lib search path."""
            if hasattr(self, '_m_nodeflib'):
                return self._m_nodeflib

            self._m_nodeflib = (self.value & 2048) != 0
            return getattr(self, '_m_nodeflib', None)


    class SectionHeaderFlags(KaitaiStruct):
        def __init__(self, value, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.value = value
            self._read()

        def _read(self):
            pass

        @property
        def merge(self):
            """might be merged."""
            if hasattr(self, '_m_merge'):
                return self._m_merge

            self._m_merge = (self.value & 16) != 0
            return getattr(self, '_m_merge', None)

        @property
        def mask_os(self):
            """OS-specific."""
            if hasattr(self, '_m_mask_os'):
                return self._m_mask_os

            self._m_mask_os = (self.value & 267386880) != 0
            return getattr(self, '_m_mask_os', None)

        @property
        def exclude(self):
            """section is excluded unless referenced or allocated (Solaris)."""
            if hasattr(self, '_m_exclude'):
                return self._m_exclude

            self._m_exclude = (self.value & 134217728) != 0
            return getattr(self, '_m_exclude', None)

        @property
        def mask_proc(self):
            """Processor-specific."""
            if hasattr(self, '_m_mask_proc'):
                return self._m_mask_proc

            self._m_mask_proc = (self.value & 4026531840) != 0
            return getattr(self, '_m_mask_proc', None)

        @property
        def strings(self):
            """contains nul-terminated strings."""
            if hasattr(self, '_m_strings'):
                return self._m_strings

            self._m_strings = (self.value & 32) != 0
            return getattr(self, '_m_strings', None)

        @property
        def os_non_conforming(self):
            """non-standard OS specific handling required."""
            if hasattr(self, '_m_os_non_conforming'):
                return self._m_os_non_conforming

            self._m_os_non_conforming = (self.value & 256) != 0
            return getattr(self, '_m_os_non_conforming', None)

        @property
        def alloc(self):
            """occupies memory during execution."""
            if hasattr(self, '_m_alloc'):
                return self._m_alloc

            self._m_alloc = (self.value & 2) != 0
            return getattr(self, '_m_alloc', None)

        @property
        def exec_instr(self):
            """executable."""
            if hasattr(self, '_m_exec_instr'):
                return self._m_exec_instr

            self._m_exec_instr = (self.value & 4) != 0
            return getattr(self, '_m_exec_instr', None)

        @property
        def info_link(self):
            """'sh_info' contains SHT index."""
            if hasattr(self, '_m_info_link'):
                return self._m_info_link

            self._m_info_link = (self.value & 64) != 0
            return getattr(self, '_m_info_link', None)

        @property
        def write(self):
            """writable."""
            if hasattr(self, '_m_write'):
                return self._m_write

            self._m_write = (self.value & 1) != 0
            return getattr(self, '_m_write', None)

        @property
        def link_order(self):
            """preserve order after combining."""
            if hasattr(self, '_m_link_order'):
                return self._m_link_order

            self._m_link_order = (self.value & 128) != 0
            return getattr(self, '_m_link_order', None)

        @property
        def ordered(self):
            """special ordering requirement (Solaris)."""
            if hasattr(self, '_m_ordered'):
                return self._m_ordered

            self._m_ordered = (self.value & 67108864) != 0
            return getattr(self, '_m_ordered', None)

        @property
        def tls(self):
            """section hold thread-local data."""
            if hasattr(self, '_m_tls'):
                return self._m_tls

            self._m_tls = (self.value & 1024) != 0
            return getattr(self, '_m_tls', None)

        @property
        def group(self):
            """section is member of a group."""
            if hasattr(self, '_m_group'):
                return self._m_group

            self._m_group = (self.value & 512) != 0
            return getattr(self, '_m_group', None)


    class PhdrTypeFlags(KaitaiStruct):
        def __init__(self, value, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.value = value
            self._read()

        def _read(self):
            pass

        @property
        def read(self):
            if hasattr(self, '_m_read'):
                return self._m_read

            self._m_read = (self.value & 4) != 0
            return getattr(self, '_m_read', None)

        @property
        def write(self):
            if hasattr(self, '_m_write'):
                return self._m_write

            self._m_write = (self.value & 2) != 0
            return getattr(self, '_m_write', None)

        @property
        def execute(self):
            if hasattr(self, '_m_execute'):
                return self._m_execute

            self._m_execute = (self.value & 1) != 0
            return getattr(self, '_m_execute', None)

        @property
        def mask_proc(self):
            if hasattr(self, '_m_mask_proc'):
                return self._m_mask_proc

            self._m_mask_proc = (self.value & 4026531840) != 0
            return getattr(self, '_m_mask_proc', None)


    class DtFlagValues(KaitaiStruct):
        """
        .. seealso::
           Figure 5-11: DT_FLAGS values - https://refspecs.linuxbase.org/elf/gabi4+/ch5.dynamic.html
        
        
        .. seealso::
           Source - https://github.com/golang/go/blob/48dfddbab3/src/debug/elf/elf.go#L1079-L1095
        
        
        .. seealso::
           Source - https://docs.oracle.com/en/operating-systems/solaris/oracle-solaris/11.4/linkers-libraries/dynamic-section.html#GUID-4336A69A-D905-4FCE-A398-80375A9E6464__CHAPTER7-TBL-5
        """
        def __init__(self, value, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.value = value
            self._read()

        def _read(self):
            pass

        @property
        def bind_now(self):
            """all relocations for this object must be processed before returning
            control to the program
            """
            if hasattr(self, '_m_bind_now'):
                return self._m_bind_now

            self._m_bind_now = (self.value & 8) != 0
            return getattr(self, '_m_bind_now', None)

        @property
        def origin(self):
            """object may reference the $ORIGIN substitution string."""
            if hasattr(self, '_m_origin'):
                return self._m_origin

            self._m_origin = (self.value & 1) != 0
            return getattr(self, '_m_origin', None)

        @property
        def textrel(self):
            """relocation entries might request modifications to a non-writable segment."""
            if hasattr(self, '_m_textrel'):
                return self._m_textrel

            self._m_textrel = (self.value & 4) != 0
            return getattr(self, '_m_textrel', None)

        @property
        def static_tls(self):
            """object uses static thread-local storage scheme."""
            if hasattr(self, '_m_static_tls'):
                return self._m_static_tls

            self._m_static_tls = (self.value & 16) != 0
            return getattr(self, '_m_static_tls', None)

        @property
        def symbolic(self):
            """symbolic linking."""
            if hasattr(self, '_m_symbolic'):
                return self._m_symbolic

            self._m_symbolic = (self.value & 2) != 0
            return getattr(self, '_m_symbolic', None)


    @property
    def sh_idx_lo_os(self):
        if hasattr(self, '_m_sh_idx_lo_os'):
            return self._m_sh_idx_lo_os

        self._m_sh_idx_lo_os = 65312
        return getattr(self, '_m_sh_idx_lo_os', None)

    @property
    def sh_idx_lo_reserved(self):
        if hasattr(self, '_m_sh_idx_lo_reserved'):
            return self._m_sh_idx_lo_reserved

        self._m_sh_idx_lo_reserved = 65280
        return getattr(self, '_m_sh_idx_lo_reserved', None)

    @property
    def sh_idx_hi_proc(self):
        if hasattr(self, '_m_sh_idx_hi_proc'):
            return self._m_sh_idx_hi_proc

        self._m_sh_idx_hi_proc = 65311
        return getattr(self, '_m_sh_idx_hi_proc', None)

    @property
    def sh_idx_lo_proc(self):
        if hasattr(self, '_m_sh_idx_lo_proc'):
            return self._m_sh_idx_lo_proc

        self._m_sh_idx_lo_proc = 65280
        return getattr(self, '_m_sh_idx_lo_proc', None)

    @property
    def sh_idx_hi_os(self):
        if hasattr(self, '_m_sh_idx_hi_os'):
            return self._m_sh_idx_hi_os

        self._m_sh_idx_hi_os = 65343
        return getattr(self, '_m_sh_idx_hi_os', None)

    @property
    def sh_idx_hi_reserved(self):
        if hasattr(self, '_m_sh_idx_hi_reserved'):
            return self._m_sh_idx_hi_reserved

        self._m_sh_idx_hi_reserved = 65535
        return getattr(self, '_m_sh_idx_hi_reserved', None)


