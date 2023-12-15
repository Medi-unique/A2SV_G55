class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        output=defaultdict(int)
        for cpdomain in cpdomains:
            repitition,domain=cpdomain.split()
            domain=domain.split('.')
            for i in range(len(domain)):
                subdomain=".".join(domain[i:])
                output[subdomain]+=int(repitition)
            print(output)
        result=[]
        for subdomain,repitition in output.items():
            result.append(str(repitition)+' '+subdomain)
        

            
             # for name in values:

        return result
        