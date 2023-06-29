# plutus
Plutus is a tool that is made ready for the purpose of monitoring your server's processes and identifying strange processes on UNIX based operating systems.     

### TODO
1. monitor network
    1. traffics incoming and outgoing [DONE]
    2. suspicious IPs [DONE]
2. monitor processes
   1. Cronjob Process Monitoring [DONE]
   2. SystemCTL Services Monitoring [DONE]
   3. Linux Program Processes Monitoring 
3. suspicious file scan
   1. File Information Retrieval [DONE]
   2. Static Analysis [PARTIALLY-DONE]
      1. File Information through online-sources such as Virus-Total [DONE]
      2. Suspicious strings retrieval on binaries and executables. [PARTIALLY-DONE]
      3. Identify if file executable is safe or malicious.
      4. Export all imported libraries that are in the executable/binary.
      5. Export all functions in the executables/binaries.
   3. Malicious Binary Type Identifier