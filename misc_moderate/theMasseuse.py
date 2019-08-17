#  The Masseuse: A popular masseuse receives a sequence of back-to-back appointment requests
# and is debating which ones to accept. She needs a 15-minute break between appointments and
# therefore she cannot accept any adjacent requests. Given a sequence of back to-back appointment requests (all multiples of 15 minutes, none overlap, and none can be moved), find the optimal
# (highest total booked minutes) set the masseuse can honor. Return the number of minutes.
# EXAMPLE
# Input: {30, 15, 60, 75, 45, 15, 15, 45}
# Output:180 minutes ({30, 60, 45, 45}).

def driver(arr):
    def getOptimalBookingTime(completeArr,startIndex,endIndex):
        arr = completeArr[startIndex:endIndex]
        if(len(arr) == 0):
            return arr
        elif len(arr) ==1:
            return arr
        elif len(arr) ==2:
            return [max(arr)]
        else:
            optimalSubSolution = cache.get('{}_{}'.format(startIndex,endIndex),-1)
            if(optimalSubSolution == -1):
                #the choice of selecting the first element
                subSolution1 = [arr[0]] + getOptimalBookingTime(completeArr,startIndex+2,endIndex)
                #the choice of not selecting the first element
                subSolution2 = getOptimalBookingTime(completeArr,startIndex+1,endIndex)
                # Mistake : Do not memoize suboptimal solutions
                # cache.update({'{}_{}'.format(startIndex+2,endIndex):subSolution1})
                # cache.update({'{}_{}'.format(startIndex+1,endIndex):subSolution2})
                result = subSolution1 if sum(subSolution1)>sum(subSolution2) else subSolution2
                # Memoize the optimal solution
                cache.update({'{}_{}'.format(startIndex,endIndex):result})
                return result
            else:
                return optimalSubSolution

    cache = {}
    selections = getOptimalBookingTime(arr,0,len(arr))
    print(selections)
    print(sum(selections))

arr = [30, 15, 60, 75, 45, 15, 15, 45]
driver(arr)