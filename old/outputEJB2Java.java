    public static Collection<TaskGroupDTO> findAll(){
        String hql = "from TaskGroupDTO where deleteStatus = 0";
        return (Collection<TaskGroupDTO>) HibernateUtil.queryForList(hql);
    }
    public static TaskGroupDTO findByAlphaId(String alphaId, Integer rootObjectId, Integer rootObjectType){
        String hql = "from TaskGroupDTO where alphaId = ?and rootObjectId = ?and rootObjectType = ?and deleteStatus = 0";
        // TODO: Check that parameter order matches query, then delete this.
        return (TaskGroupDTO) HibernateUtil.queryForSingleResult(hql, alphaId, rootObjectId, rootObjectType);
    }
    public static TaskGroupDTO findByName(String name, Integer rootObjectId, Integer rootObjectType){
        String hql = "from TaskGroupDTO where name = ?and rootObjectId = ?and rootObjectType = ?and deleteStatus = 0";
        // TODO: Check that parameter order matches query, then delete this.
        return (TaskGroupDTO) HibernateUtil.queryForSingleResult(hql, name, rootObjectId, rootObjectType);
    }
    public static Collection<TaskGroupDTO> findByBusinessObject(Integer rootObjectId, Integer rootObjectType){
        String hql = "from TaskGroupDTO where rootObjectId = ? and rootObjectType = ? and deleteStatus = 0";
        // TODO: Check that parameter order matches query, then delete this.
        return (Collection<TaskGroupDTO>) HibernateUtil.queryForList(hql, rootObjectId, rootObjectType);
    }
