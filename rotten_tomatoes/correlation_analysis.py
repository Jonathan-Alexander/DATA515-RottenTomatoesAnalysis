class CorrelationAnalysis:
    
    def __init__(self, d):
        self.data = d
        
    def corr_matrix(self, subset = None):
        if subset == None:
            data = self.data
        else:
            data = self.data[subset]
            
        return data.corr()
    
    def plot_heatmap(self, subset = None):
        sns.heatmap(self.corr_matrix(subset).round(2), annot=True, vmax=1, vmin=-1)
        return
    
    def corr_coef(self, a, b):
        return data[a].corr(data[b])

        
    