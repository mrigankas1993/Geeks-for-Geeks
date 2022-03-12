
int kthDiff(int a[], int n, int k)
{
    vector<int> vect1;
    for(int i = 0;i < n; i++){
        for(int j = i + 1; j < n;j++){
            int e = abs(a[j] - a[i]);
            vect1.push_back(e);
        }
    }
    sort(vect1.begin(), vect1.end());
    k -= 1;
    return vect1[k];
}
