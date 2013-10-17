/*
 * Copyright 2004 by Bricsnet FM
 *
 * This software is the confidential and proprietary information
 * of Bricsnet FM. (Confidential Information).  You shall not
 * disclose such Confidential Information and shall use it only
 * in accordance with the terms of the license agreement you
 * entered into with Bricsnet FM.
 *
 * $Id: LeaseEJB.java 37316 2009-05-13 22:44:32Z mabraham $
 */

package com.bricsnet.lease.ejb.lease.entity;

import java.sql.Timestamp;
import java.util.Date;

import javax.ejb.EJBException;
import javax.ejb.EntityBean;

import com.bricsnet.core.session.uidgenerator.UIDGeneratorServiceRemote;
import com.bricsnet.core.session.uidgenerator.UIDGeneratorServiceRemoteHome;
import com.bricsnet.core.session.uidgenerator.UIDGeneratorServiceUtil;

/**
 * @ejb.permission role-name="Member"
 * @ejb.bean
 *         description="Lease Entity Bean"
 *         type="CMP"
 *         name="Lease"
 *         view-type="local"
 *         display-name="Lease EJB"
 *         primkey-field="id"
 *         schema="Lease"
 *         jndi-name="ejb/Lease"
 *         cmp-version="${ejb.cmp.version}"
 * @ejb.value-object
 *         name="Lease"
 *         extends="com.bricsnet.lease.ejb.lease.entity.BaseLeaseDTO"
 *      implements="com.bricsnet.core.util.model.type.Auditable,com.bricsnet.core.util.model.StatefulBusinessObject"
 *         match="*"
 * @ejb.transaction
 *         type="Required"
 * @ejb.persistence
 *         table-name="Lease"
 * @ejb.pk class="java.lang.Integer"
 * @jboss.persistence
 *      datasource="java:jdbc/BuildingCenterBizDS_baseline"
 *      datasource-mapping="MS SQLSERVER"
 * @orion.bean
 *         data-source="jdbc/BuildingCenterBizDS_baseline"
 *
 * @ejb.ejb-external-ref
 *      ref-name="ejb/UIDGeneratorService"
 *      jndi-name="ejb/UIDGeneratorService"
 *      link="UIDGeneratorService"
 *      home="com.bricsnet.core.session.uidgenerator.UIDGeneratorServiceRemoteHome"
 *      business="com.bricsnet.core.session.uidgenerator.UIDGeneratorServiceRemote"
 *      view-type="remote"
 *      type="Session"
 *
 * @ejb.finder
 *         signature="java.util.Collection findAll()"
 *         query="select object(c) from Lease as c"
 *
 * @ejb.finder
 *         signature="Lease findByAlphaId(java.lang.String alphaId)"
 *         query="select object(c) from Lease as c where c.alphaId = ?1 and c.deleteStatus=0"
 *
 * @ejb.finder
 *         signature="java.util.Collection findByMasterId(java.lang.Integer masterId)"
 *         query="select object(c) from Lease as c where c.masterId = ?1"
 *
 * @ejb.finder
 *      signature="java.util.Collection findByPropertyId(java.lang.Integer propertyId)"
 *      query="select object(c) from Lease as c where c.propertyId = ?1 and c.deleteStatus=0"
 *
 * @ejb.finder
 *      signature="java.util.Collection findByTaxGroupId(java.lang.Integer taxGroupId)"
 *      query="select object(c) from Lease as c where c.taxGroupId = ?1 and c.deleteStatus=0"
 *
 * @author <a href="mailto:daniel.hew@bricsnet.com">Daniel Hew</a>
 */
public abstract class LeaseEJB implements EntityBean {

    //private static Logger log = Logger.getLogger(LeaseEJB.class);
    private static String TABLE_NAME = "Lease";

    /**
     * @ejb.interface-method
     */
    public abstract LeaseDTO getLeaseDTO();

    /**
     * @ejb.interface-method
     */
    public abstract void setLeaseDTO(LeaseDTO dto);

    /**
     * @ejb.pk-field
     * @ejb.interface-method
     * @ejb.persistent-field
     * @bricsnet.localize format="#"
     * @bricsnet.hiddenFromHistory
     */
    public abstract Integer getId();

    public abstract void setId(Integer value);

    /**
     * @ejb.interface-method
     * @ejb.persistent-field
     * @bricsnet.localize format="#"
     * @bricsnet.hiddenFromHistory
     */
    public abstract Integer getMasterId();

    public abstract void setMasterId(Integer value);

    /**
     * @ejb.interface-method
     * @ejb.persistent-field
     */
    public abstract String getAlphaId();

    public abstract void setAlphaId(String value);

    /**
     * @ejb.interface-method
     * @ejb.persistent-field
     */
    public abstract String getName();

    public abstract void setName(String value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     * @bricsnet.localize format="#"
     */
    public abstract Integer getStatus();

    public abstract void setStatus(Integer value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     * @bricsnet.localize format="#"
     * @bricsnet.hiddenFromHistory
     */
    public abstract Integer getFasbStatus();

    public abstract void setFasbStatus(Integer value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     * @bricsnet.localize format="#"
     */
    public abstract Integer getType();

    public abstract void setType(Integer value);

    /**
     * @ejb.interface-method
     * @ejb.persistent-field
     * @bricsnet.localize format="#"
     */
    public abstract Integer getLsePosition();

    public abstract void setLsePosition(Integer value);

    /**
     * @ejb.interface-method
     * @ejb.persistent-field
     * @bricsnet.localize format="#"
     */
    public abstract Integer getOccupancyStatus();

    public abstract void setOccupancyStatus(Integer value);

    /**
     * @ejb.interface-method
     * @ejb.persistent-field
     * @bricsnet.localize format="#"
     */
    public abstract Integer getCategory();

    public abstract void setCategory(Integer value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     * @bricsnet.localize format="#"
     * @bricsnet.hiddenFromHistory
     */
    public abstract Integer getLegalEntityId();

    public abstract void setLegalEntityId(Integer value);

    /**
     * @ejb.interface-method
     * @ejb.persistent-field
     */
    public abstract Date getStartDate();

    public abstract void setStartDate(Date value);

    /**
     * @ejb.interface-method
     * @ejb.persistent-field
     */
    public abstract Date getStartDateCurrent();

    public abstract void setStartDateCurrent(Date value);

    /**
     * @ejb.interface-method
     * @ejb.persistent-field
     */
    public abstract Date getEndDateCurrent();

    public abstract void setEndDateCurrent(Date value);

    /**
     * @ejb.interface-method
     * @ejb.persistent-field
     */
    public abstract Date getEndDateOriginal();

    public abstract void setEndDateOriginal(Date value);

    /**
     * @ejb.interface-method
     * @ejb.persistent-field
     */
    public abstract Date getPossessionDate();

    public abstract void setPossessionDate(Date value);

    /**
     * @ejb.interface-method
     * @ejb.persistent-field
     */
    public abstract Date getStartDateRent();

    public abstract void setStartDateRent(Date value);

    /**
     * @ejb.interface-method
     * @ejb.persistent-field
     */
    public abstract Date getSignedDate();

    public abstract void setSignedDate(Date value);

    /**
     * @ejb.interface-method
     * @ejb.persistent-field
     */
    public abstract Date getMoveInDate();

    public abstract void setMoveInDate(Date value);

    /**
     * @ejb.interface-method
     * @ejb.persistent-field
     */
    public abstract Date getMoveOutDate();

    public abstract void setMoveOutDate(Date value);

    /**
     * @ejb.interface-method
     * @ejb.persistent-field
     */
    public abstract Date getOpenDate();

    public abstract void setOpenDate(Date value);

    /**
     * @ejb.interface-method
     * @ejb.persistent-field
     */
    public abstract Date getLastAuditDate();

    public abstract void setLastAuditDate(Date value);

    /**
     * @ejb.interface-method
     * @ejb.persistent-field
     */
    public abstract boolean getMonthly();

    public abstract void setMonthly(boolean value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     */
    public abstract boolean getIsIndefiniteTerm();

    public abstract void setIsIndefiniteTerm(boolean value);

    /**
     * @ejb.interface-method
     * @ejb.persistent-field
     */
    public abstract Date getStartDateMonthly();

    public abstract void setStartDateMonthly(Date value);

    /**
     * @ejb.interface-method
     * @ejb.persistent-field
     */
    public abstract Double getUseableArea();

    public abstract void setUseableArea(Double value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     */
    public abstract Double getRentableArea();

    public abstract void setRentableArea(Double value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     */
    public abstract Double getSellableArea();

    public abstract void setSellableArea(Double value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     */
    public abstract Double getAllocatedArea();

    public abstract void setAllocatedArea(Double value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     */
    public abstract Double getProrataShare();

    public abstract void setProrataShare(Double value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     * @bricsnet.localize format="#,##0.00"
     */
    public abstract Double getCredit();

    public abstract void setCredit(Double value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     * @bricsnet.localize format="#"
     */
    public abstract Integer getMeasureStandard();

    public abstract void setMeasureStandard(Integer value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     */
    public abstract Integer getTotalParkingSpaces();

    public abstract void setTotalParkingSpaces(Integer value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     */
    public abstract Integer getAssignedParkingSpaces();

    public abstract void setAssignedParkingSpaces(Integer value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     * @bricsnet.localize format="#"
     */
    public abstract Integer getTaxGroupId();

    public abstract void setTaxGroupId(Integer value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     * @bricsnet.localize format="#"
     * @bricsnet.hiddenFromHistory
     */
    public abstract Integer getPropertyId();

    public abstract void setPropertyId(Integer value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     * @ejb.persistence column-name="currency"
     * @bricsnet.localize format="#"
     */
    public abstract Integer getCurrencyId();

    public abstract void setCurrencyId(Integer value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     */
    public abstract String getComments();

    public abstract void setComments(String value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     * @bricsnet.hiddenFromHistory
     */
    public abstract boolean getHasNote();

    public abstract void setHasNote(boolean value);

    /* Audit fields */
    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     * @bricsnet.localize format="#"
     * @bricsnet.hiddenFromHistory
     */
    public abstract Integer getLastUpdatedBy();

    public abstract void setLastUpdatedBy(Integer value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     * @bricsnet.hiddenFromHistory
     */
    public abstract Timestamp getLastUpdatedOn();

    public abstract void setLastUpdatedOn(Timestamp value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     * @bricsnet.hiddenFromHistory
     */
    public abstract Integer getVersion();

    public abstract void setVersion(Integer value);

    /* End Audit Fields */

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     */
    public abstract Double getTotalObligation();

    public abstract void setTotalObligation(Double value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     */
    public abstract int getDeleteStatus();

    public abstract void setDeleteStatus(int value);

    /**
     * @ejb.interface-method
     * @ejb.persistent-field
     * @bricsnet.localize format="#"
     */
    public abstract Integer getLandLord();

    public abstract void setLandLord(Integer value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     * @bricsnet.localize format="#,##0.00"
     */
    public abstract Double getOverallCap();

    public abstract void setOverallCap(Double value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     * @bricsnet.localize format="#,##0.00"
     */
    public abstract double getAdminFee();

    public abstract void setAdminFee(double value);

    /**
     * @ejb.persistent-field
     * @ejb.interface-method
     * @bricsnet.localize format="#,##0.00"
     */
    public abstract Double getDiscountRate();

    public abstract void setDiscountRate(Double value);

    /**
     * @ejb.create-method
     */
    public Integer ejbCreate(LeaseDTO dto) throws javax.ejb.CreateException {

        try {
            UIDGeneratorServiceRemoteHome uidHome = UIDGeneratorServiceUtil
                    .getHome();
            UIDGeneratorServiceRemote uidRemote = uidHome.create();
            Integer key = uidRemote.getUniqueId(TABLE_NAME);

            //log.info(" creating Lease: "+key+" "+dto.getName());
            this.setId(key);
            this.setLeaseDTO(dto);

        } catch (Exception e) {
            throw new EJBException(e);
        }
        return null; // Return null when using CMP
    }

    public void ejbPostCreate(LeaseDTO dto) {
    }
}
