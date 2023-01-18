class Solution:
    def check_empty_hands(self, count_dict):
        for k, v in count_dict.items():
            if v:
                return False
        return True

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        smallest_hand_ind = 0
        count_dict = {}
        for cur_hand in hand:
            try:
                count_dict[cur_hand]+=1
            except:
                count_dict[cur_hand]=1
        
        
        sorted_hands = sorted(list(count_dict.keys()))
        smallest_hand_ind = 0
        
        while smallest_hand_ind<len(sorted_hands):
            smallest_hand = sorted_hands[smallest_hand_ind]
            smallest_hand_count = count_dict[smallest_hand]
            if smallest_hand_count==0:
                smallest_hand_ind+=1
                continue
            for checking_hand in range(smallest_hand, smallest_hand+groupSize):
                if checking_hand not in count_dict.keys() or count_dict[checking_hand]<smallest_hand_count:
                    return False
                count_dict[checking_hand]-=smallest_hand_count

        return self.check_empty_hands(count_dict)