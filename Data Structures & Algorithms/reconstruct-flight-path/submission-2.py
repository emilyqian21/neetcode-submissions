class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #Keep walking until you're stuck. When you're stuck, record the airport and go back.
        #STACK --> store cities to visit 
        stack = ["JFK"]
        itinerary = []

        # sort tickets
        tickets.sort(reverse = True)
        # adj dict
        start2dest = defaultdict(list)
        for start, dest in tickets:
            start2dest[start].append(dest) # {buf: hou, jfk:buf, hou: sea}
        
        while stack: # while there is city to visit
            cur_start = stack[-1] #Only pop it once all outgoing edges have been used.
            if not start2dest[cur_start]:
                stack.pop()
                itinerary.append(cur_start)
            if start2dest[cur_start]:
                next_city_in_order = start2dest[cur_start].pop()
                stack.append(next_city_in_order)
        return itinerary[::-1]

        