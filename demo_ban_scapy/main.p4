#include "tables.p4"


control ingress {
    apply(proto_lookup);
    apply(bad_lookup);
    
    if(standard_metadata.egress_spec != 4){
    	if(not valid(my_path_header)) {
       		apply(path_lookup);
    	}
    	apply(forward);
	}
	
    //apply(bad_lookup);
}
