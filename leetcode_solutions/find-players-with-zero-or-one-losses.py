class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners={}
        losers={}
        players=set()

        answer=[[],[]]
        for winner,loser in matches:
            players.add(winner)
            players.add(loser)
            winners[winner]=winners.get(winner,0)+1
            losers[loser]=losers.get(loser,0)+1
        for i in players:
            if i not in losers:
                answer[0].append(i)
            elif  losers.get(i,0)==1:
                answer[1].append(i)
        return [sorted(answer[0]),sorted(answer[1])]




   

       
        
        


        