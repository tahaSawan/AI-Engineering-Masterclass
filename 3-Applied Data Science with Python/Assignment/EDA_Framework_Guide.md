# 📊 Complete EDA Framework Guide
## Universal Steps for Any Data Science Problem

---

## ✅ What We've Covered in This Project

### Phase 1: Data Understanding & Quality Assessment
- ✅ **Load and Inspect Data** - Shape, columns, data types, sample rows
- ✅ **Missing Values Check** - Using `isna()` and `notna()` functions
- ✅ **Data Quality Checks** - Duplicates, negative values, zero values, unique values
- ✅ **Data Type Validation** - Checking and converting data types

### Phase 2: Data Cleaning & Preprocessing
- ✅ **Handle Missing Values** - Recommendations for drop vs fill
- ✅ **Data Transformation** - Date parsing, string cleaning
- ✅ **Normalization** - Min-Max scaling applied

### Phase 3: Univariate Analysis
- ✅ **Descriptive Statistics** - Mean, median, mode, std dev, min, max
- ✅ **Distribution Analysis** - Histograms, box plots
- ✅ **Skewness & Kurtosis** - Distribution shape analysis
- ✅ **Categorical Analysis** - Value counts, frequency distributions

### Phase 4: Bivariate Analysis
- ✅ **Categorical vs Numerical** - Group comparisons (State vs Sales, Group vs Sales)
- ✅ **Categorical vs Categorical** - State-Group analysis, Time-Group analysis
- ✅ **Correlation Analysis** - Sales vs Unit correlation
- ✅ **Scatter Plots** - Relationship visualization

### Phase 5: Multivariate Analysis
- ✅ **Heatmaps** - State-Group, Time-Group, Time-State matrices
- ✅ **Multi-dimensional Analysis** - Pivot tables, grouped analysis

### Phase 6: Time Series Analysis
- ✅ **Temporal Patterns** - Daily, weekly, monthly trends
- ✅ **Time-based Aggregations** - Reports by time periods
- ✅ **Peak/Off-peak Analysis** - Time-of-day patterns

### Phase 7: Insights & Recommendations
- ✅ **Key Findings** - State rankings, group rankings
- ✅ **Actionable Insights** - Strategic recommendations

---

## 📋 Complete EDA Framework (For Any Problem)

### **PHASE 1: DATA UNDERSTANDING & QUALITY ASSESSMENT**

#### Step 1: Load and Inspect Data
```python
# Always start here
df = pd.read_csv('your_file.csv')
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(df.head())
print(df.info())
print(df.describe())
```

**What to check:**
- Number of rows and columns
- Column names and data types
- Sample data (first/last few rows)
- Memory usage

#### Step 2: Data Quality Checks
```python
# Missing values
print(df.isna().sum())
print(df.isna().sum() / len(df) * 100)  # Percentage

# Duplicates
print(f"Duplicates: {df.duplicated().sum()}")

# Data types
print(df.dtypes)

# Unique values in categorical columns
for col in categorical_cols:
    print(f"{col}: {df[col].nunique()} unique values")
```

**What to check:**
- Missing values (count and percentage)
- Duplicate rows
- Data type consistency
- Invalid entries (negative values, out of range)
- Unique value counts

---

### **PHASE 2: DATA CLEANING & PREPROCESSING**

#### Step 3: Handle Missing Values
```python
# Option 1: Drop (if < 5% and random)
df = df.dropna()

# Option 2: Fill numerical (mean, median, mode)
df['column'].fillna(df['column'].mean(), inplace=True)

# Option 3: Fill categorical (mode)
df['column'].fillna(df['column'].mode()[0], inplace=True)

# Option 4: Forward/Backward fill (time series)
df['column'].fillna(method='ffill', inplace=True)
```

**Decision criteria:**
- **Drop**: < 5% missing, random pattern, won't affect analysis
- **Fill**: > 5% missing, systematic pattern, important variable

#### Step 4: Handle Outliers
```python
# Method 1: IQR Method
Q1 = df['column'].quantile(0.25)
Q3 = df['column'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df['column'] < lower) | (df['column'] > upper)]

# Method 2: Z-score Method
from scipy import stats
z_scores = np.abs(stats.zscore(df['column']))
outliers = df[z_scores > 3]

# Visualize
sns.boxplot(y=df['column'])
```

**Decision criteria:**
- **Remove**: Data entry errors, < 1% of data
- **Transform**: Log transform, square root
- **Keep**: Legitimate extreme values, important for analysis

#### Step 5: Data Transformation
```python
# Normalization (0-1 range)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['normalized'] = scaler.fit_transform(df[['column']])

# Standardization (mean=0, std=1)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df['standardized'] = scaler.fit_transform(df[['column']])

# Encoding categorical
df = pd.get_dummies(df, columns=['categorical_col'])

# Date parsing
df['date'] = pd.to_datetime(df['date'])
```

---

### **PHASE 3: UNIVARIATE ANALYSIS (Single Variable)**

#### Step 6: Numerical Variables Analysis
```python
# Descriptive statistics
print(df['column'].describe())
print(f"Mean: {df['column'].mean()}")
print(f"Median: {df['column'].median()}")
print(f"Mode: {df['column'].mode()[0]}")
print(f"Std Dev: {df['column'].std()}")
print(f"Skewness: {df['column'].skew()}")
print(f"Kurtosis: {df['column'].kurtosis()}")

# Visualizations
sns.histplot(df['column'], kde=True)  # Distribution
sns.boxplot(y=df['column'])  # Outliers
sns.violinplot(y=df['column'])  # Distribution + outliers
```

**What to analyze:**
- Central tendency (mean, median, mode)
- Variability (std dev, range, IQR)
- Distribution shape (skewness, kurtosis)
- Outliers

#### Step 7: Categorical Variables Analysis
```python
# Frequency analysis
print(df['column'].value_counts())
print(df['column'].value_counts(normalize=True) * 100)  # Percentages

# Visualizations
df['column'].value_counts().plot(kind='bar')
sns.countplot(data=df, x='column')
```

**What to analyze:**
- Value counts and frequencies
- Most/least common categories
- Category distribution

---

### **PHASE 4: BIVARIATE ANALYSIS (Two Variables)**

#### Step 8: Numerical vs Numerical
```python
# Correlation
correlation = df['col1'].corr(df['col2'])
print(f"Correlation: {correlation:.4f}")

# Correlation matrix
corr_matrix = df[numerical_cols].corr()
sns.heatmap(corr_matrix, annot=True)

# Scatter plot
plt.scatter(df['col1'], df['col2'])
sns.regplot(x='col1', y='col2', data=df)  # With regression line
```

**What to analyze:**
- Correlation strength and direction
- Linear/non-linear relationships
- Outliers in relationships

#### Step 9: Categorical vs Numerical
```python
# Group statistics
print(df.groupby('categorical')['numerical'].agg(['mean', 'median', 'std']))

# Visualizations
sns.boxplot(x='categorical', y='numerical', data=df)
sns.violinplot(x='categorical', y='numerical', data=df)
sns.barplot(x='categorical', y='numerical', data=df)
```

**What to analyze:**
- Differences between groups
- Group distributions
- Statistical significance (t-test, ANOVA)

#### Step 10: Categorical vs Categorical
```python
# Contingency table
crosstab = pd.crosstab(df['cat1'], df['cat2'])
print(crosstab)

# Chi-square test
from scipy.stats import chi2_contingency
chi2, p_value, dof, expected = chi2_contingency(crosstab)

# Visualizations
sns.heatmap(crosstab, annot=True)
crosstab.plot(kind='bar', stacked=True)
```

**What to analyze:**
- Association between categories
- Independence testing (chi-square)
- Patterns in combinations

---

### **PHASE 5: MULTIVARIATE ANALYSIS (Multiple Variables)**

#### Step 11: Advanced Visualizations
```python
# Pair plot (all numerical variables)
sns.pairplot(df[numerical_cols])

# Correlation matrix
sns.heatmap(df[numerical_cols].corr(), annot=True, cmap='coolwarm')

# 3D scatter plot (if needed)
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['x'], df['y'], df['z'])
```

**What to analyze:**
- Multiple variable relationships
- Feature interactions
- Dimensionality reduction opportunities

---

### **PHASE 6: TIME SERIES ANALYSIS (If Applicable)**

#### Step 12: Temporal Patterns
```python
# Set date as index
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

# Time-based aggregations
daily = df.resample('D').sum()
weekly = df.resample('W').sum()
monthly = df.resample('M').sum()

# Trends
df['value'].plot()  # Line plot
sns.lineplot(x='date', y='value', data=df)

# Seasonality
df.groupby(df.index.month)['value'].mean().plot()  # Monthly pattern
df.groupby(df.index.dayofweek)['value'].mean().plot()  # Weekly pattern
```

**What to analyze:**
- Trends (increasing/decreasing)
- Seasonality (monthly, weekly patterns)
- Cyclical patterns
- Anomalies over time

---

### **PHASE 7: INSIGHTS & RECOMMENDATIONS**

#### Step 13: Key Findings Summary
```python
# Create summary
findings = {
    'Data Quality': 'No missing values, 5% outliers',
    'Key Patterns': 'Strong correlation between X and Y',
    'Anomalies': 'Unusual spike in December',
    'Distribution': 'Right-skewed, requires transformation'
}
```

**What to document:**
- Data quality assessment
- Key patterns discovered
- Relationships found
- Anomalies identified
- Distribution characteristics

#### Step 14: Actionable Insights
```python
# Business recommendations
recommendations = [
    'Focus on high-performing segments',
    'Address outliers in production data',
    'Consider feature engineering for skewed variables',
    'Monitor time-based patterns'
]
```

**What to provide:**
- Business recommendations
- Next steps for analysis
- Suggestions for feature engineering
- Model preparation insights

---

## 🎯 Quick Reference Checklist

Use this checklist for ANY new dataset:

- [ ] **Load data** and check shape, columns, data types
- [ ] **Check missing values** (isna(), notna())
- [ ] **Check duplicates** and data quality issues
- [ ] **Handle missing values** (drop or fill)
- [ ] **Detect and handle outliers** (IQR or Z-score)
- [ ] **Transform data** (normalize, encode, parse dates)
- [ ] **Univariate analysis** (descriptive stats, distributions)
- [ ] **Bivariate analysis** (correlations, group comparisons)
- [ ] **Multivariate analysis** (heatmaps, pair plots)
- [ ] **Time series analysis** (if applicable)
- [ ] **Document findings** and provide recommendations

---

## 💡 Key Principles

1. **Always start with data quality** - Garbage in, garbage out
2. **Visualize everything** - A picture is worth 1000 words
3. **Understand before transforming** - Know why you're doing something
4. **Document your decisions** - Future you will thank you
5. **Think about the business** - Connect analysis to real-world impact

---

## 🔄 Adapt Based on Problem Type

### **Classification Problems:**
- Focus on target variable distribution
- Analyze class imbalance
- Feature importance analysis
- Categorical vs target relationships

### **Regression Problems:**
- Focus on target variable distribution
- Correlation with features
- Outlier impact on target
- Feature scaling importance

### **Clustering Problems:**
- All features distribution
- Feature scaling critical
- Correlation analysis
- Dimensionality considerations

### **Time Series Problems:**
- Temporal patterns essential
- Seasonality detection
- Trend analysis
- Stationarity checks

---

## 📚 Remember

**EDA is iterative** - You may need to go back and re-analyze after cleaning.

**Context matters** - What's an outlier in one problem might be important in another.

**Business understanding** - Always connect your analysis to business objectives.

**Documentation** - Your future self (and teammates) will thank you for clear documentation.

---

**This framework works for 90% of data science problems. Adapt it based on your specific needs!**
