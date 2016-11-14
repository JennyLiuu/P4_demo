#include "parsers.p4"

counter test_counter {
    type: packets;
    static: forward;
    instance_count: 16384;
}

table proto_lookup {
    reads {
        ipv4.protocol: exact;
    }

    actions {
        action_proto_lookup;
        _nop;
    }

}

action _nop(){
}

action action_proto_lookup(out_port) {
    modify_field(standard_metadata.egress_spec, out_port);
}

table bad_lookup {
    reads {
        ethernet.src: exact;
    }

    actions {
        action_bad_lookup;
        _drop;
    }

}

action _drop() {
    drop();
}

action action_bad_lookup(out_port) {
    modify_field(standard_metadata.egress_spec, out_port);
}


table path_lookup {
    reads {
        ethernet.dst: exact;
        ethernet.src: exact;
    }

    actions {
        action_path_lookup;
    }

}

action action_path_lookup(path_no) {
    add_header(my_path_header);
    modify_field(my_path_header.preamble, 0xc0ffee);
    modify_field(my_path_header.path, path_no);
}

table forward {
    reads {
        my_path_header.path: exact;
    }

    actions {
        action_forward;
        action_forward_pop_path;
    }
    size : 16384;
}


action action_forward(out_port) {
    modify_field(standard_metadata.egress_spec, out_port);
}

action action_forward_pop_path(out_port,idx) {
    modify_field(standard_metadata.egress_spec, out_port);
    count(test_counter, idx);
    remove_header(my_path_header);
}





