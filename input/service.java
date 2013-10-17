/*
 * $Id: DirectoryEntryServiceEJB.java 41186 2011-04-14 16:43:43Z jlau $
 */
package com.bricsnet.core.dal.person;

import java.util.List;

import javax.ejb.EJBException;
import javax.ejb.SessionBean;
import javax.ejb.SessionContext;

import com.bricsnet.core.entity.person.DirectoryEntryLocal;
import com.bricsnet.core.entity.person.DirectoryEntryUtil;
import com.bricsnet.core.util.Constants;
import com.bricsnet.core.util.model.type.BizObject;
import com.bricsnet.core.util.model.type.ChildObject;
import com.bricsnet.core.util.observer.BusinessObjectObserver;
import com.bricsnet.core.util.security.policy.BricsnetPolicy;
import com.bricsnet.core.util.security.principal.UserPrincipal;
import com.bricsnet.core.util.session.BaseAncillaryObjectSessionBean;
import com.bricsnet.core.util.struts.ValidationMethod;

/**
 *
 * @ejb.permission role-name="Member"
 * @ejb.bean type="Stateless" description="DirectoryEntry Session Bean"
 *           name="DirectoryEntryService" jndi-name="ejb/DirectoryEntryService"
 *           type="Stateless" view-type="both"
 *           display-name="DirectoryEntryServiceEJB"
 * @ejb.interface extends="javax.ejb.EJBObject,
 *      com.bricsnet.core.util.model.service.ChildObjectService<com.bricsnet.core.entity.person.DirectoryEntryDTO>"
 * @ejb.transaction type="Required"
 * @ejb.ejb-ref
 *      ejb-name="DirectoryEntry"
 *      view-type="local"
 *      ref-name="ejb/DirectoryEntryLocal"
 *      link="DirectoryEntryLocal"
 *
 * @author <a href="mailto:david.hamilton@bricsnet.com">David J. Hamilton</a>
 */
public abstract class DirectoryEntryService extends BaseAncillaryObjectSessionBean
        implements SessionBean {

    /**
     * Gets a DirectoryEntryDTO object based on its id (primary key) and the
     * isExtended boolean value. An extended dto contains all the objects that
     * are represented by foreign keys in the table.
     *
     * @param id The id (primary key) of the object to get.
     * @param isExtended If true get the extended attributes.
     *
     * @ejb.interface-method
     * @ejb.transaction type="${build.ejb.transaction.readonly}"
     */
    public DirectoryEntryDTO getDTO(Integer id, boolean isExtended) {
        try {
            UserPrincipal p = getUserPrincipal();
            DirectoryEntryDTO dto = DirectoryEntryDTOFactory.getDTO(id,
                                                                    p,
                                                                    isExtended);
            BricsnetPolicy.checkPermission(p, dto);
            return dto;
        } catch (EJBException e) {
            throw e;
        } catch (Exception e) {
            throw new EJBException(e);
        }
    }

    /**
     * Returns the list of directory entries for the root object specified by
     * <tt>rootId</tt> and <tt>rootType</tt>, with extended attributes set
     * IFF <tt>extended</tt> is true.
     *
     * @param rootId
     * @param rootType
     * @param extended
     * @return
     *
     * @ejb.interface-method
     * @ejb.transaction type="${build.ejb.transaction.readonly}"
     */
    public List<DirectoryEntryDTO> getAllForParent(Integer rootId,
                                                   Integer rootType,
                                                   boolean extended) {
        try {
            return DirectoryEntryDTOFactory.getAllForParent(rootId,
                                                            rootType,
                                                            getUserPrincipal(),
                                                            extended);
        } catch (EJBException e) {
            throw e;
        } catch (Exception e) {
            throw new EJBException(e);
        }
    }

    /**
     * Creates a new DirectoryEntryDTO with a blank custom attrib hierarchy
     * (contains AttribGroupRefDTOs, AttribDTOs, and empty AttribValueDTOs).
     * Does not create anything in the database, just produces a blank DTO.
     *
     * @ejb.interface-method
     * @ejb.transaction type="${build.ejb.transaction.readonly}"
     */
    public DirectoryEntryDTO getNewDTO() {
        return (DirectoryEntryDTO) getNewDTO(DirectoryEntryDTO.class);
    }

    /**
     * Convenience method for <code>create(d, null, false);</code>
     *
     * @see #create(BizObject, ValidationMethod[], boolean)
     * @ejb.interface-method
     * @ejb.transaction type="Required"
     */
    public DirectoryEntryDTO create(DirectoryEntryDTO d) {
        return create(d, null, false);
    }

    /**
     * Creates a Directory Entry.
     *
     * @ejb.interface-method
     * @ejb.transaction type="Required"
     */
    public DirectoryEntryDTO create(Object obj,
                                    ValidationMethod[] vmethods,
                                    boolean extended) {
        return create((DirectoryEntryDTO) obj, vmethods, extended);
    }

    /**
     * Creates a Directory Entry.
     *
     * @ejb.interface-method
     * @ejb.transaction type="Required"
     */
    public DirectoryEntryDTO create(BizObject obj,
                                    ValidationMethod[] vmethods,
                                    boolean extended) {
        return create((DirectoryEntryDTO) obj, vmethods, extended);
    }

    /**
     * Creates a Directory Entry. Uses the localization map to set properties in
     * the bean, but if the map is empty it will not effect the bean.
     *
     * @param dto Contains the data to write to the database
     * @ejb.interface-method
     * @ejb.transaction type="Required"
     */
    public DirectoryEntryDTO create(DirectoryEntryDTO dto,
                                    ValidationMethod[] list,
                                    boolean extended) {
        try {
            UserPrincipal p = getUserPrincipal();

            BricsnetPolicy.checkPermission(p, dto);

            BusinessObjectObserver.beforeCreate(dto, null, p);

            DirectoryEntryDTO created;
            created = DirectoryEntryUtil.getLocalHome().create(dto)
                    .getDirectoryEntryDTO();

            BusinessObjectObserver.afterCreate(created, null, p);

            return created;
        } catch (EJBException e) {
            throw e;
        } catch (Exception e) {
            throw new EJBException(e);
        }
    }

    /**
     * Updates a Directory Entry.
     *
     * @ejb.interface-method
     * @ejb.transaction type="Required"
     */
    public void update(Object obj, ValidationMethod[] vm) {
        update((DirectoryEntryDTO) obj, vm);
    }

    /**
     * Updates a Directory Entry.
     *
     * @ejb.interface-method
     * @ejb.transaction type="Required"
     */
    public void update(BizObject obj, ValidationMethod[] vm) {
        update((DirectoryEntryDTO) obj, vm);
    }

    /**
     * Updates a Directory Entry.
     *
     * @ejb.interface-method
     * @ejb.transaction type="Required"
     */
    public void update(DirectoryEntryDTO dto, ValidationMethod[] list) {
        try {
            UserPrincipal p = getUserPrincipal();

            BricsnetPolicy.checkPermission(p, dto);

            DirectoryEntryDTO prior =
                DirectoryEntryDTOFactory.getDTO(dto.getId(), null, false);
            BusinessObjectObserver.beforeUpdate(prior, dto, null, p);

            DirectoryEntryUtil.getLocalHome().findByPrimaryKey(dto.getId())
            .setDirectoryEntryDTO(dto);
            storeCustomAttributes(dto);

            BusinessObjectObserver.afterUpdate(prior, dto, null, p);
        } catch(EJBException e) {
            throw e;
        } catch(Exception e) {
            throw new EJBException(e);
        }
    }

    /**
     * Deletes a DirectoryEntry. The record remains in the database and
     * the delete flag is set (soft delete).
     *
     * @ejb.interface-method
     * @ejb.transaction type="Required"
     */
    public void delete(Object dto) {
        delete(((DirectoryEntryDTO)dto).getId());
    }

    /**
     * Deletes a DirectoryEntry. The record remains in the database and
     * the delete flag is set (soft delete).
     *
     * @ejb.interface-method
     * @ejb.transaction type="Required"
     */
    public void delete(BizObject dto) {
        delete(((DirectoryEntryDTO)dto).getId());
    }

    /**
     * Deletes a DirectoryEntryDTO.
     *
     * @ejb.interface-method
     * @ejb.transaction type="Required"
     */
    public void delete(DirectoryEntryDTO dto) {
        delete(dto.getId());
    }

    /**
     * Deletes a Directory Entry.
     *
     * @param id The id (primary key) of the object to delete.
     *
     * @ejb.interface-method
     * @ejb.transaction type="Required"
     */
    public void delete(Integer id) {
        try {
            DirectoryEntryLocal ejb =
                DirectoryEntryUtil.getLocalHome().findByPrimaryKey(id);
            DirectoryEntryDTO dto = ejb.getDirectoryEntryDTO();
            UserPrincipal p = getUserPrincipal();
            BricsnetPolicy.checkPermission(p, dto);
            dto.setDeleteStatus(Constants.DELETED);
            BusinessObjectObserver.beforeRemove(dto, p);
            ejb.setDirectoryEntryDTO(dto);
            BusinessObjectObserver.afterRemove(dto, p);
        } catch(EJBException e) {
            throw e;
        } catch(Exception e) {
            throw new EJBException(e);
        }
    }

    /**
     * Set the associated session context. The container calls this method after
     * the instance creation. See the javax.ejb.SessionBean interface.
     */
    public void setSessionContext(SessionContext context) {
        super.setSessionContext(context);
    }

    /**
     * @ejb.interface-method
     * @ejb.transaction type="${build.ejb.transaction.readonly}"
     */
    public List<DirectoryEntryDTO> getChildDTOsOf(BizObject bo) {
        return getAllForParent(bo.getObjectId(), bo.getObjectType(), true);
    }

    /**
     * @ejb.interface-method
     * @ejb.transaction type="${build.ejb.transaction.readonly}"
     */
    public DirectoryEntryDTO setParentChildReference(DirectoryEntryDTO child, BizObject parent) {
        child.setRefObjectId(parent.getObjectId());
        child.setRefObjectType(parent.getObjectType());
        return child;
    }

    /**
     * @ejb.interface-method
     * @ejb.transaction type="${build.ejb.transaction.readonly}"
     */
    public DirectoryEntryDTO setParentChildReference(ChildObject child, BizObject parent) {
        return setParentChildReference((DirectoryEntryDTO) child, parent);
    }

    /**
     * @ejb.interface-method
     * @ejb.transaction type="${build.ejb.transaction.readonly}"
     */
    public DirectoryEntryDTO setParentChildReference(Object child, BizObject parent) {
        return setParentChildReference((DirectoryEntryDTO) child, parent);
    }
}
