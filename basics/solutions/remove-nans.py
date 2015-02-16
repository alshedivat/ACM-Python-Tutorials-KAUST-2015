nan_rows = np.any(np.isnan(auto), axis=1)
auto = auto[~auto_nan_rows,]
