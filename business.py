def reach_rank(df, upper, lower):
    from_upper = (df >= upper).sum(axis='columns')
    less_lower = (df < lower).sum(axis='columns')
    reach = (from_upper >= 6) & (less_lower == 0)
    
    return reach.astype(int)


class HLRanking:
    def __init__(self, df):
        self.df = df
        self.df_score = df.iloc[:, -8:]
        
        # Excellent reach
        self.reach_excel = reach_rank(self.df_score, upper=9, lower=8)
        
        # Good reach
        self.reach_good = reach_rank(self.df_score, upper=8, lower=6.5)
        
        # Average reach
        self.reach_avg = reach_rank(self.df_score, upper=6.5, lower=5)
        
        # Good reach
        self.reach_ok = reach_rank(self.df_score, upper=5, lower=3.5)
        
        # Total reach
        self.reach_total = (self.reach_excel + 
                            self.reach_good +
                            self.reach_avg +
                            self.reach_ok)
        
        mapping = {4: 'Xuất sắc',
                   3: 'Tốt',
                   2: 'Khá',
                   1: 'Đạt',
                   0: 'Không Đạt'}
        
        self.rank = self.reach_total.map(mapping)
        
    def get_rank(self):
        
        result = self.df.iloc[:, :3]
        result['Xếp loại học lực'] = self.rank
        
        return result
    
    def get_stat(self):
        
        result = self.rank.value_counts()
        
        return result
        
        
        
        
        

        
        
        
        

        