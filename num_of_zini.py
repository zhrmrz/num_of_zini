import numpy as np
class Soloution:
    def num_of_zini(self,num_of_rows_cols,nums):
        num_of_rows_cols=num_of_rows_cols.split()
        result=0
        nums=np.array(nums.split())
        nums=nums.reshape(int(num_of_rows_cols[0]),int(num_of_rows_cols[1]))

        for i in range(1,int(num_of_rows_cols[0])-1):
            for j in range(1,int(num_of_rows_cols[1])-1):
                if nums[i][j]>nums[i-1][j] and nums[i][j]>nums[i+1][j] and nums[i][j+1]>nums[i][j] and nums[i][j-1]>nums[i][j]:
                    result+=1
                elif nums[i][j]<nums[i-1][j] and nums[i][j]<nums[i+1][j] and nums[i][j+1]<nums[i][j] and nums[i][j-1]<nums[i][j]:
                    result+=1

        return result


if __name__ == '__main__':
    p1=Soloution()
    print(p1.num_of_zini('4 4','1 2 4 1 7 4 1 1 1 3 2 4 1 4 1 1'))
