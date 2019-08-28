# Backtracking
# Should be of the form -> adding something, backtrack - recursive and then removing 

# Python code to check valid possible IP 
  
# Function checks wheather IP digits 
# are valid or not. 
def is_valid(ip): 
  
    # Spliting by "." 
    ip = ip.split(".") 
      
    # Checking for the corner cases 
    for i in ip: 
        if len(i) > 3 or int(i) < 0 or int(i) > 255: 
            return False
        if len(i) > 1 and int(i) == 0: 
            return False
        if len(i) > 1 and int(i) != 0 and i[0] == '0': 
            return False
    return True
  
# Function converts string to IP address 
def convert(s): 
    sz = len(s) 
  
    # Check for string size 
    if sz > 12: 
        return [] 
    snew = s 
    l = [] 

    # Generating different combinations. 
    for i in range(1, sz - 2): 
        for j in range(i + 1, sz - 1): 
            for k in range(j + 1, sz): 
                snew = snew[:k] + "." + snew[k:] 
                snew = snew[:j] + "." + snew[j:] 
                snew = snew[:i] + "." + snew[i:] 
                  
                # Check for the validity of combination 
                if is_valid(snew): 
                    l.append(snew) 
                snew = s 
    return l  
  
# Driver code          
A = "25525511135"
B = "25505011535"
print(convert(A)) 
print(convert(B)) 


# Java code - backtracking
# class Solution {
#     private final static int MAX_VALUE = 255;
    
#     public List<String> restoreIpAddresses(String s) {
#         List<String> res = new ArrayList<>();
        
#         if (s.length() == 0) {
#             return res;
#         }
        
#         List<String> path = new ArrayList<>();
#         int len = s.length();
#         dfs(0, 4, len, s, path, res);
        
#         return res;
#     }
    
#     private void dfs(int start, int count, int len, String s, List<String> path, List<String> res) {
        
#         int numOfDigitsLeft = len - start;
        
#         if (3*count <  numOfDigitsLeft || numOfDigitsLeft < count) { 
#             return;
#         }
        
#         if (count == 0) {
#             res.add(String.join(".", path));
#             return;
#         }
        
#         for (int size = 1; size <= 3; size++) {
#             if (start + size - 1 >= len ) {
#                 continue;
#             }
            
#             String num = s.substring(start, start + size);
            
#             if (Integer.valueOf(num) <= MAX_VALUE
#                 && (num.length() == 1 || num.charAt(0) != '0')) {
                
#                 path.add(num);
#                 dfs(start + size, count - 1, len, s, path, res);
#                 path.remove(path.size() - 1);
#             }
#         }
#     }
# }