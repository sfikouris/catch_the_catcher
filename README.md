# Catch_the_catcher

## Analyze packets

### GSM
 Protocol to follow -> gsm_a.dtap
 expand this protocol I follow packets with GPRS mobility management messages and mobility managment messages.
 
 ### todo
 	-> I will work also with the SIPs for neighbors and etc, but later. 
 	-> Check radio resources management messages for the channel release case, to be Normal event (?) 
 	-> Track a legitment attachment and right down the messages that are excgange. Then find a way to check if at every new attachment those steps are similar. 
/**General info about the subfield of the protocol that I will collect and analyze**/

### MM: gsm_a.dtap.msg_mm_type 
	Location updating request/accept
	identity request/response	
	authentication request/response
    IMSI detach indication 
		
### GMM: gsm_a.dtap.msg_gmm_type
	attach/detach request
	authentication and ciphering req/resp
    attach complete
    attach accept


/**Specific values of the subfields that I will look for more details **/

### MM 
##### Authentication request
	Check the values of -> Authentication Parameter RAND - UMTS challenge or GSM challenge
					=> RAND value: if it has at all a hash value or is empty or even a value that looks strange.
			     -> Authentication Parameter AUTN (UMTS and EPS authentication challenge)
			     		=> Element ID
			     		=> Length
			     		=> AUTN value
			     			> SQN xor AK
			     			> AMF
			     			> MAC		

   -> Authentication response
   	At this phase I will not check for the response. No need.
   
   -> Identity request 
   	Check the value of -> Identity type, IMSI or T-MSI (probably here is asking only for imsi but need to be double check).
   	Check the next Identity request for IMEI no need ?
