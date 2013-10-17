    public static AccountDTO findByAlphaId(String alphaId,Integer parentId){
        String hql = "from AccountDTO where alphaId = ? and coaId = ? and deleteStatus =0";
        // TODO: Check that parameter order matches query, then delete this.
        return (AccountDTO) HibernateUtil.queryForSingleResult(hql, alphaId, parentId);
    }
