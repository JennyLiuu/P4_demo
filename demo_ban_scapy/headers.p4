header_type my_path_header_t {
    fields {
        preamble: 24;
        path: 16;
    }
}

header_type ethernet_t {
    fields {
    	dst: 16;
        src: 16;
        etherType : 16;
    }
}

header_type ipv4_t {
    fields {
        //version : 4;
        //ihl : 4;
        //tos : 8;
        protocol : 8;
        srcAddr : 32;
        dstAddr: 32;
    }
}

header my_path_header_t my_path_header;
header ethernet_t ethernet;
header ipv4_t ipv4;
