#include "headers.p4"

parser start {
    return select(current(0, 24)) {
        0xc0ffee: parse_my_path_header;
        default: parse_ethernet;
    }
}

parser parse_my_path_header {
    extract(my_path_header);
    return parse_ethernet;
}

parser parse_ethernet {
    extract(ethernet);
    return parse_ipv4;
}

parser parse_ipv4 {
    extract(ipv4);
    return ingress;
}