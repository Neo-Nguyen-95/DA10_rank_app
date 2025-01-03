def reach_rank(df, upper, lower):
    from_upper = (df >= upper).sum(axis='columns')
    less_lower = (df < lower).sum(axis='columns')
    reach = (from_upper >= 6) & (less_lower == 0)
    
    return reach.astype(int)


class HLRanking:
    def __init__(self, df, lower_xs=6.5):
        self.df = df
        self.df_score = df.iloc[:, -8:]
        
        # Excellent reach
        self.reach_excel = reach_rank(self.df_score, upper=9, lower=lower_xs)
        
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
        
        mapping_KQHT = {4: 'Tốt',
                        3: 'Tốt',
                        2: 'Khá',
                        1: 'Đạt',
                        0: 'Không Đạt'}
        
        mapping_DH = {4: 'Xuất sắc',
                      3: 'Giỏi',
                      2: 'Không xét',
                      1: 'Không xét',
                      0: 'Không xét'}
        
             
        self.rank_KQHT = self.reach_total.map(mapping_KQHT)
        self.rank_DH = self.reach_total.map(mapping_DH)
        
    def get_rank(self):
        
        result = self.df.iloc[:, :2]
        result['Kết quả học tập'] = self.rank_KQHT
        result['Danh hiệu'] = self.rank_DH
        
        return result
    
    def get_stat_KQHT(self):
        
        result = self.rank_KQHT.value_counts()
        
        return result
    
    def get_stat_DH(self):
        
        result = self.rank_DH.value_counts()
        
        return result
        
        
        
        
        

        
        
        
        

        